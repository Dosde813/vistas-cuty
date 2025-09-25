# tests/request_client.py
import sys, requests, time, random
from datetime import datetime

TARGET = sys.argv[1] if len(sys.argv)>1 else "http://tu-servidor/registro"
RUN_ID = sys.argv[2] if len(sys.argv)>2 else f"run-{int(time.time())}"
UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36",
]

def main():
    # envía entre 1 y 3 visitas con pequeño jitter desde este runner
    visits = random.randint(1,3)
    for v in range(visits):
        ua = random.choice(UA_LIST)
        headers = {"User-Agent": ua, "Referer": "https://example.com", "Origin": "https://example.com"}
        params = {"run_id": RUN_ID, "visit": v+1}
        try:
            r = requests.get(TARGET, params=params, headers=headers, timeout=20)
            print(f"{datetime.utcnow().isoformat()} - sent visit {v+1}/{visits} status={r.status_code}")
        except Exception as e:
            print("error:", e)
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    main()
