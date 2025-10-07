# from flask import Flask, jsonify, request, Response, stream_with_context
# from flask_cors import CORS
# import json, time, random
# from datetime import datetime
# from collections import Counter

# app = Flask(__name__)
# CORS(app)

# DATA_FILE = "gamex_data.json"

# def load_data():
#     with open(DATA_FILE) as f:
#         return json.load(f)

# # -----------------------------
# # 📊 Módulo 1: Métricas básicas
# # -----------------------------
# @app.route("/api/gamex/access", methods=["GET"])
# def access_data():
#     data = load_data()
#     return jsonify(data["access_logs"])

# @app.route("/api/gamex/sales", methods=["GET"])
# def sales_data():
#     data = load_data()
#     return jsonify(data["sales"])

# @app.route("/api/gamex/games", methods=["GET"])
# def games_data():
#     data = load_data()
#     return jsonify(data["games_added"])

# @app.route("/api/gamex/metrics", methods=["GET"])
# def gamex_metrics():
#     data = load_data()

#     total_users = sum([x["users"] for x in data["access_logs"]])
#     avg_users = round(total_users / len(data["access_logs"]), 2)

#     total_sales = sum([x["amount"] for x in data["sales"]])
#     avg_sales = round(total_sales / len(data["sales"]), 2)

#     total_games = len(data["games_added"])

#     return jsonify({
#         "avg_daily_users": avg_users,
#         "total_sales": total_sales,
#         "avg_daily_sales": avg_sales,
#         "games_added": total_games
#     })

# # -----------------------------
# # 🔍 Módulo 3: Insights
# # -----------------------------
# @app.route("/api/gamex/insights", methods=["GET"])
# def gamex_insights():
#     data = load_data()

#     # Dev que mais publicou jogos
#     devs = [g["dev"] for g in data["games_added"]]
#     top_dev, top_dev_count = Counter(devs).most_common(1)[0]

#     # Dia de maior faturamento
#     top_sale = max(data["sales"], key=lambda x: x["amount"])

#     # Correlação simples entre acessos e vendas (mesma data)
#     access_map = {a["date"]: a["users"] for a in data["access_logs"]}
#     sales_map = {s["date"]: s["amount"] for s in data["sales"]}

#     correlation = []
#     for date in sales_map:
#         if date in access_map:
#             correlation.append({"date": date, "users": access_map[date], "sales": sales_map[date]})

#     return jsonify({
#         "top_dev": {"name": top_dev, "games_published": top_dev_count},
#         "highest_sales_day": top_sale,
#         "access_sales_correlation": correlation[:10]  # mostra só os 10 primeiros
#     })

# # -----------------------------
# # 📄 Módulo 4: Relatório inteligente
# # -----------------------------
# @app.route("/api/gamex/report", methods=["GET"])
# def gamex_report():
#     data = load_data()

#     total_users = sum([x["users"] for x in data["access_logs"]])
#     total_sales = sum([x["amount"] for x in data["sales"]])
#     total_games = len(data["games_added"])

#     avg_users = round(total_users / len(data["access_logs"]), 2)
#     avg_sales = round(total_sales / len(data["sales"]), 2)

#     # Top dev
#     devs = [g["dev"] for g in data["games_added"]]
#     top_dev, top_dev_count = Counter(devs).most_common(1)[0]

#     # Melhor dia de vendas
#     top_sale = max(data["sales"], key=lambda x: x["amount"])

#     report_text = f"""
#     📊 Relatório Inteligente da Plataforma GameX ({datetime.utcnow().date()})

#     👥 Usuários totais no período: {total_users}
#     👥 Média de acessos por dia: {avg_users}

#     💰 Faturamento total: R$ {total_sales}
#     💵 Faturamento médio por dia: R$ {avg_sales}
#     📈 Melhor dia de vendas: {top_sale['date']} (R$ {top_sale['amount']})

#     🎮 Jogos adicionados no período: {total_games}
#     🏆 Dev mais ativo: {top_dev} ({top_dev_count} jogos publicados)

#     🔎 Insights:
#     - Crescimento consistente em acessos e vendas.
#     - Forte correlação entre aumento de acessos e faturamento.
#     - Devs ativos impulsionam diretamente as vendas.
#     """

#     return jsonify({"report": report_text})

# # -----------------------------
# # 🔴 Módulo 2: Stream de eventos
# # -----------------------------
# def event_stream():
#     events = ["new_access", "new_sale", "new_game"]
#     while True:
#         event = random.choice(events)
#         payload = {"event": event, "timestamp": datetime.utcnow().isoformat()}
#         if event == "new_access":
#             payload["users"] = random.randint(1, 10)
#         elif event == "new_sale":
#             payload["amount"] = round(random.uniform(50, 200), 2)
#         elif event == "new_game":
#             payload["dev"] = random.choice(["Dev1", "Dev2", "Dev3"])
#             payload["title"] = random.choice(["Game X", "Game Y", "Game Z"])
#         yield f"data: {json.dumps(payload)}\n\n"
#         time.sleep(5)

# @app.route("/api/gamex/stream")
# def stream():
#     return Response(stream_with_context(event_stream()), mimetype="text/event-stream")

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

# @app.route("/api/gamex/lessons", methods=["GET"])
# def gamex_lessons():
#     data = load_data()

#     total_users = sum([x["users"] for x in data["access_logs"]])
#     avg_users = round(total_users / len(data["access_logs"]), 2)

#     total_sales = sum([x["amount"] for x in data["sales"]])
#     avg_sales = round(total_sales / len(data["sales"]), 2)

#     total_games = len(data["games_added"])

#     lessons = []

#     # Exemplo de regra: se a média de acessos for alta
#     if avg_users > 300:
#         lessons.append("Campanhas de engajamento foram eficazes para atrair usuários.")
#     else:
#         lessons.append("É necessário investir mais em marketing para aumentar os acessos.")

#     # Exemplo de regra: se o faturamento médio for consistente
#     if avg_sales > 2000:
#         lessons.append("Estratégia de preços e catálogo de jogos foram bem recebidos pelo público.")
#     else:
#         lessons.append("Avaliar ajustes no modelo de monetização para melhorar o faturamento.")

#     # Exemplo: quantidade de jogos publicados
#     if total_games >= 10:
#         lessons.append("A participação dos desenvolvedores foi ativa, contribuindo para a diversidade de títulos.")
#     else:
#         lessons.append("Necessário incentivar devs a publicarem mais jogos na plataforma.")

#     report_text = f"""
#     📘 Lições Aprendidas - GameX ({datetime.utcnow().date()})

#     👥 Média de acessos por dia: {avg_users}
#     💵 Faturamento médio por dia: R$ {avg_sales}
#     🎮 Total de jogos publicados: {total_games}

#     🔑 Lições principais:
#     - {lessons[0]}
#     - {lessons[1]}
#     - {lessons[2]}
#     """

#     return jsonify({"lessons_learned": report_text})




# # # app.py
# # from flask import Flask, jsonify, request, Response, stream_with_context
# # from flask_cors import CORS01
# # import csv, json, time, random
# # from datetime import datetime


# # app = Flask(__name__)
# # CORS(app)  # permite chamadas do Angular dev

# # CSV_FILE = "sensors_data.csv"

# # def read_csv_all():
# #     rows = []
# #     try:
# #         with open(CSV_FILE, newline='') as f:
# #             reader = csv.DictReader(f)
# #             for r in reader:
# #                 r['temperature'] = float(r['temperature'])
# #                 r['energy'] = float(r['energy'])
# #                 r['occupancy'] = int(r['occupancy'])
# #                 rows.append(r)
# #     except FileNotFoundError:
# #         pass
# #     return rows

# # @app.route("/api/sensors/latest", methods=["GET"])
# # def latest():
# #     rows = read_csv_all()
# #     if not rows:
# #         return jsonify({}), 200
# #     return jsonify(rows[-1]), 200

# # @app.route("/api/sensors/history", methods=["GET"])
# # def history():
# #     rows = read_csv_all()
# #     return jsonify(rows), 200

# # import json

# # @app.route("/api/project/metrics")
# # def project_metrics():
# #     # carrega os dados do projeto
# #     with open("project_data.json") as f:
# #         data = json.load(f)

# #     sprints = data["sprints"]

# #     # Velocity: média de pontos entregues por sprint
# #     delivered = [s["delivered_points"] for s in sprints]
# #     velocity = sum(delivered) / len(delivered)

# #     # Earned Value (EV), Planned Value (PV), Actual Cost (AC)
# #     EV = sum([s["ev"] for s in sprints])
# #     PV = sum([s["pv"] for s in sprints])
# #     AC = sum([s["ac"] for s in sprints])

# #     # CPI e SPI
# #     cpi = EV / AC if AC > 0 else 0
# #     spi = EV / PV if PV > 0 else 0

# #     # Burndown (pontos restantes por sprint)
# #     total_planned = sum([s["planned_points"] for s in sprints])
# #     burndown = []
# #     remaining = total_planned
# #     for i, s in enumerate(sprints, 1):
# #         remaining -= s["delivered_points"]
# #         burndown.append({"sprint": i, "remaining": max(0, remaining)})

# #     return jsonify({
# #         "velocity": round(velocity, 2),
# #         "cpi": round(cpi, 2),
# #         "spi": round(spi, 2),
# #         "burndown": burndown
# #     })


# # @app.route("/api/report/status", methods=["POST"])
# # def report():
# #     data = request.get_json() or {}
# #     report_text = f"Relatório de status - {datetime.utcnow().date()}\n"
# #     report_text += f"Velocity estimada: {data.get('velocity', 24)}\n"
# #     report_text += "Resumo: Trabalho em andamento, sem bloqueios críticos. Próximas ações: finalizar integração do dashboard e scripts de simulação.\n"
# #     return jsonify({"report": report_text}), 200

# # # SSE stream simples para demo
# # def sensor_stream():
# #     while True:
# #         r = {
# #             "timestamp": datetime.utcnow().isoformat(),
# #             "temperature": round(random.uniform(20, 27), 2),
# #             "energy": round(random.uniform(80, 200), 2),
# #             "occupancy": random.randint(0, 10)
# #         }
# #         yield f"data: {json.dumps(r)}\n\n"
# #         time.sleep(5)

# # @app.route("/api/stream/sensors", methods=["GET"])
# # def stream():
# #     return Response(stream_with_context(sensor_stream()), mimetype="text/event-stream")

# # if __name__ == "__main__":
# #     app.run(debug=True, port=5000)

from flask import Flask, jsonify, request
import json, os
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

genai.configure(api_key="SUA_CHAVE_API_GEMINI")

DB_PATH = "db.txt"

# Cria o banco fictício se não existir
if not os.path.exists(DB_PATH):
    data = {
        "dashboard": {
            "acessos": 2456,
            "faturamento": 32190.75,
            "jogos_inseridos": 145
        },
        "monitoramento": {
            "usuarios_online": 128,
            "vendas_dia": 42,
            "novos_jogos": 3
        },
        "insights": {
            "tendencias": [
                "Jogos indie com estética retrô estão em alta.",
                "Promoções aumentam o engajamento em 35%.",
                "Jogos multiplayer mantêm usuários ativos por mais tempo."
            ],
            "kpis": {
                "retencao": 0.87,
                "satisfacao": 0.93,
                "tempo_medio_sessao": "18min"
            }
        },
        "riscos": [
            {"risco": "Instabilidade no servidor", "impacto": "Alto"},
            {"risco": "Baixa taxa de conversão em dias úteis", "impacto": "Médio"}
        ]
    }
    with open(DB_PATH, "w") as f:
        f.write(json.dumps(data))

def read_db():
    with open(DB_PATH, "r") as f:
        return json.loads(f.read())

@app.route("/api/dashboard")
def get_dashboard():
    return jsonify(read_db()["dashboard"])

@app.route("/api/monitoramento")
def get_monitoramento():
    return jsonify(read_db()["monitoramento"])

@app.route("/api/insights")
def get_insights():
    return jsonify(read_db()["insights"])

@app.route("/api/relatorio", methods=["POST"])
def gerar_relatorio():
    dados = read_db()
    prompt = f"""
    Gere um relatório corporativo para a plataforma GameX.
    Inclua:
    - Resumo geral dos acessos ({dados['dashboard']['acessos']})
    - Faturamento total (R${dados['dashboard']['faturamento']})
    - Jogos inseridos ({dados['dashboard']['jogos_inseridos']})
    - Monitoramento (usuários online, vendas do dia)
    - Principais insights e riscos.

    Use um tom profissional e breve, no estilo de relatório executivo.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({"relatorio": response.text})
    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
