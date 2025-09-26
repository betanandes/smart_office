# app.py
from flask import Flask, jsonify, request, Response, stream_with_context
from flask_cors import CORS
import csv, json, time, random
from datetime import datetime


app = Flask(__name__)
CORS(app)  # permite chamadas do Angular dev

CSV_FILE = "sensors_data.csv"

def read_csv_all():
    rows = []
    try:
        with open(CSV_FILE, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                r['temperature'] = float(r['temperature'])
                r['energy'] = float(r['energy'])
                r['occupancy'] = int(r['occupancy'])
                rows.append(r)
    except FileNotFoundError:
        pass
    return rows

@app.route("/api/sensors/latest", methods=["GET"])
def latest():
    rows = read_csv_all()
    if not rows:
        return jsonify({}), 200
    return jsonify(rows[-1]), 200

@app.route("/api/sensors/history", methods=["GET"])
def history():
    rows = read_csv_all()
    return jsonify(rows), 200

import json

@app.route("/api/project/metrics")
def project_metrics():
    # carrega os dados do projeto
    with open("project_data.json") as f:
        data = json.load(f)

    sprints = data["sprints"]

    # Velocity: média de pontos entregues por sprint
    delivered = [s["delivered_points"] for s in sprints]
    velocity = sum(delivered) / len(delivered)

    # Earned Value (EV), Planned Value (PV), Actual Cost (AC)
    EV = sum([s["ev"] for s in sprints])
    PV = sum([s["pv"] for s in sprints])
    AC = sum([s["ac"] for s in sprints])

    # CPI e SPI
    cpi = EV / AC if AC > 0 else 0
    spi = EV / PV if PV > 0 else 0

    # Burndown (pontos restantes por sprint)
    total_planned = sum([s["planned_points"] for s in sprints])
    burndown = []
    remaining = total_planned
    for i, s in enumerate(sprints, 1):
        remaining -= s["delivered_points"]
        burndown.append({"sprint": i, "remaining": max(0, remaining)})

    return jsonify({
        "velocity": round(velocity, 2),
        "cpi": round(cpi, 2),
        "spi": round(spi, 2),
        "burndown": burndown
    })


@app.route("/api/report/status", methods=["POST"])
def report():
    data = request.get_json() or {}
    report_text = f"Relatório de status - {datetime.utcnow().date()}\n"
    report_text += f"Velocity estimada: {data.get('velocity', 24)}\n"
    report_text += "Resumo: Trabalho em andamento, sem bloqueios críticos. Próximas ações: finalizar integração do dashboard e scripts de simulação.\n"
    return jsonify({"report": report_text}), 200

# SSE stream simples para demo
def sensor_stream():
    while True:
        r = {
            "timestamp": datetime.utcnow().isoformat(),
            "temperature": round(random.uniform(20, 27), 2),
            "energy": round(random.uniform(80, 200), 2),
            "occupancy": random.randint(0, 10)
        }
        yield f"data: {json.dumps(r)}\n\n"
        time.sleep(5)

@app.route("/api/stream/sensors", methods=["GET"])
def stream():
    return Response(stream_with_context(sensor_stream()), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
