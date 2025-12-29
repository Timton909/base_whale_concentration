import requests, time

def whale_concentration():
    print("Base — Whale Concentration Alert (top 10 holders >70% in young token)")
    seen = set()

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            for pair in r.json().get("pairs", []):
                addr = pair["pairAddress"]
                if addr in seen: continue

                age = time.time() - pair.get("pairCreatedAt", 0) / 1000
                if age > 300: continue  # older than 5 min

                top10 = pair.get("top10HoldersPercent", 0)
                if top10 > 70:
                    token = pair["baseToken"]["symbol"]
                    print(f"WHALE CONCENTRATION\n"
                          f"{token} — top 10 hold {top10:.1f}%\n"
                          f"Age: {age:.0f}s | Liq: ${pair['liquidity']['usd']:,.0f}\n"
                          f"https://dexscreener.com/base/{addr}\n"
                          f"→ High rug risk — few hands control supply\n"
                          f"{'WHALE DOMINANCE'*10}")
                    seen.add(addr)

        except:
            pass
        time.sleep(4.7)

if __name__ == "__main__":
    whale_concentration()
