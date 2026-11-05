import os, random, time, requests

URL = os.environ["ENLACE"]
N = int(os.environ.get("VISITAS", "2"))
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 Version/17.5 Mobile Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 Chrome/131.0 Mobile Safari/537.36",
]
s = requests.Session()
for i in range(N):
    try:
        s.get(URL, headers={"User-Agent": random.choice(UAS), "Referer": "https://www.google.com/"}, timeout=20)
    except Exception as e:
        print("fallo", e)
    time.sleep(random.uniform(12, 22))
print("ok")
