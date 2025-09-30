import re
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DB_PATH = Path("books.db")
TABLE = "books"

def load_data(db_path: Path, table: str) -> pd.DataFrame:
    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found: {db_path}")
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    return df

def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    可視化/相関分析のための特徴量を追加
      - price_gbp: 数値
      - rating: 1~5(欠損はNaN)
      - stock_qty: 在庫表記から数量を推定
    """
    out = df.copy()

    # 在庫数量の抽出
    if "stock_text" in out.columns:
        out["stock_qty"] = (
            out["stock_text"]
            .astype(str)
            .str.extract(r"(\d+)", expand=False)
            .astype(float)
        )
    else:
        out["stock_qty"] = np.nan

    # rating文字列を数値に
    rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
    if "rating" in out.columns:
        out["rating"] = out["rating"].map(rating_map).astype(float)

    # 列の存在保証
    for col in ["price_gbp", "rating"]:
        if col not in out.columns:
            out[col] = np.nan
    
    return out

def plot_histgram(df: pd.DataFrame):
    plt.figure(figsize=(7, 4))
    df["price_gbp"].dropna().plot(kind="hist", bins=30, edgecolor="black")
    plt.title("Price Distribution")
    plt.xlabel("Price (GBP)")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.show()

def plot_boxplot_by_rating(df: pd.DataFrame):
    sub = df[["price_gbp", "rating"]].dropna()
    if sub.empty:
        print("[WARN] rating/price_gbp が不足しているため箱ひげ図をスキップします")
        return
    
    plt.figure(figsize=(7, 4))
    sns.boxplot(data=sub, x="rating", y="price_gbp", showfliers=True)
    plt.title("Price by Star Rating")
    plt.xlabel("Star rating (1-5)")
    plt.ylabel("Price (GBP)")
    plt.tight_layout()
    plt.show()

def plot_corr_heatmap(df: pd.DataFrame):
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not num_cols:
        print("[WARN] 数値列が存在しないため相関ヒートマップをスキップします")
        return
    
    corr = df[num_cols].corr()
    plt.figure(figsize=(5 + 0.4*len(num_cols), 4 + 0.4*len(num_cols)))
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

def main():
    df = load_data(DB_PATH, TABLE)
    print(f"[OK] Loaded: {len(df)} rows, columns: {list(df.columns)}")

    df2 = prepare_features(df)
    print(df2[["title", "price_gbp", "rating", "stock_qty"]].head(10))

    plot_histgram(df2)
    plot_boxplot_by_rating(df2)
    plot_corr_heatmap(df2)

if __name__ == "__main__":
    main()
