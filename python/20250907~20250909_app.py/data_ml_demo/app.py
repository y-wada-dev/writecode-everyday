import io
import re
import base64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from collections import Counter

st.set_page_config(page_title="データ分析・機械学習デモ", layout="wide")


# ====== header ======
st.title("データ分析・機械学習デモ")
st.caption("CSVファイルのアップロード、基本的なデータ分析、簡単な機械学習モデルの構築を行います。")
st.markdown("このアプリは、データ分析と機械学習のデモを提供します。")

# ====== common helper functions ======
def ensure_datetaime_index(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """指定した列をDatetimeindexに変換する"""
    if col not in df.colomns:
        raise ValueError(f"指定列{col}がデータフレームに存在しません。")
    d = df.copy()
    d[col] = pd.to_datetime(d[col])
    d = d.set_index(col).sort_index()
    return d

def download_link_from_df(df: pd.DataFrame, filename: str = "data.csv", label: str = "CSVをダウンロード"):
    """データフレームをCSVとしてダウンロードするためのリンクを生成する"""
    csv = df.to_csv(index=False).encode("utf-8-sig")
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

def to_pairplot_like(df: pd.DataFrame, cols: list[str]):
    """"簡易pairplotを作成する"""
    n = len(cols)
    fig, axes = plt.subplots(n, n, figsize=(3*n, 3*n))
    for i, ci in enumerate(cols):
        for j, cj in enumerate(cols):
            ax = axes[i, j]
            if i == j:
                ax.hist(df[ci].dropna(),bins=15)
            else:
                ax.scatter(df[cj].dropna(), df[ci].dropna(), s=10, alpha=0.7)
            if i == n-1:
                ax.set_xlabel(cj)
            if j == 0:
                ax.set_ylabel(ci)
    plt.tight_layout()
    return fig

# ====== sidebar ======
st.sidebar.header("機能を選択")
page = st = st.sidebar.radio(
    "Select",
    [
        "CSVアップロードと表示",
        "時系列(CSV)",
        "散布図 & 簡易回帰",
        "分布図可視化(ヒストグラム/箱ひげ)",
        "相関ヒートマップ",
        "簡易感情分析(辞書ベース)"
    ]
)

