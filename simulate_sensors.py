# simulate_sensors.py
import csv
import random
from datetime import datetime, timedelta

CSV_FILE = "sensors_data.csv"

def generate_reading(ts=None):
    ts = ts or datetime.utcnow()
    return {
        "timestamp": ts.isoformat(),
        "temperature": round(random.uniform(20, 27) + random.choice([0, 0.5, -0.5]), 2),
        "energy": round(random.uniform(80, 200), 2),
        "occupancy": random.randint(0, 10)
    }

def append_csv(row):
    header = ["timestamp","temperature","energy","occupancy"]
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(row)

if __name__ == "__main__":
    # Gera 500 leituras com espaçamento de 30s (arquivo para dev/test)
    t = datetime.utcnow()
    for i in range(500):
        r = generate_reading(t)
        append_csv(r)
        t += timedelta(seconds=30)
    print("Arquivo gerado:", CSV_FILE)
