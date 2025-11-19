import pandas as pd
import numpy as np

BASE_CSV = "pref_temp_base.csv"
OUTPUT_CSV = "japan_temp_by_year.csv"

def main():
    base = pd.read_csv(BASE_CSV)

    years = range(2015, 2025)

    rows = []
    rng = np.random.default_rng(42)

    for year in years:
        for _, r in base.iterrows():
            base_temp = float(r["value"])

            trend = 0.15 * (year - 2015)
            noise = rng.normal(0, 1.5)

            temp = base_temp + trend + noise
            
            temp = max(35, min(75, temp))

            rows.append({
                "year": year,
                "pref_code": int(r["pref_code"]),
                "pref_name": str(r["pref_name"]),
                "temp_c": round(temp, 1)
            })
    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    print(f"[OK] {OUTPUT_CSV} 出力完了")

if __name__ == "__main__":
    main()