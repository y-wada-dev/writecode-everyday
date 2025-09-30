import re
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DB_PATH = Path("./books.db")
TABLE = "books"

def load_data(db_path: Path, table: str) -> pd.DataFrame:
    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found: {db_path}")
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    return df

def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """"
    可視化/相関分析のための特徴量を追加
      - prce_gdp: 数値
      - ranting: 1~5(欠損はNaN)
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

    
    # 列の存在保証
    for col in ["price_gdp", "rating"]:
        if col not in out.columns:
            out[col] = np.nan
    
    return out


