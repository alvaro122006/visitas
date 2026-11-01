import os, random, time, datetime, requests

URL = os.environ["ENLACE"]
DIA = datetime.date.today().day
N = min(40, 5 + DIA)
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 Version/17.5 Mobile Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 Chrome/131.0 Mobile Safari/537.36",
]
for i in range(N):
    try:
        requests.get(
            URL,
            headers={"User-Agent": random.choice(UAS), "Referer": "https://www.google.com/"},
            timeout=20,
        )
    except Exception as e:
        print("fallo", e)
    time.sleep(random.uniform(0.8, 3.0))
print("hechas", N)
