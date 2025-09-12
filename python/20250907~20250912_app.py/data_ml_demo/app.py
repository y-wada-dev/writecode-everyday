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
def ensure_datetime_index(df: pd.DataFrame, col: str) -> pd.DataFrame:
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
        "1) CSVアップロードと表示",
        "2) 時系列(CSV)",
        "3) 散布図 & 簡易回帰",
        "4) 分布図可視化(ヒストグラム/箱ひげ)",
        "5) 相関ヒートマップ",
        "6) 簡易感情分析(辞書ベース)"
    ]
)

# ====== CSVアップロードと表示 ======
if page.startswith("1)"):
    st.subheader("CSVアップロード表示")
    st.write("任意のCSVをアップロードして、列を選んでグラフ化できます。")

    file = st.file_uploader("CSVファイルを選択", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write("データプレビュー")
        st.dataframe(df.head())

        cols = df.columns.toloist()
        x_col = st.selectbox("X軸", cols, index=0)
        y_col = st.selectbox("Y軸", cols, index=min(1, len(cols)-1))
        kind = st.selectbox("種類", ["line", "scatter", "bar"])

        fig, ax = plt.subplots(figsize=(7, 4))
        if kind == "line":
            ax.plot(df[x_col], df[y_col])
        elif kind == "scatter":
            ax.scatter(df[x_col], df[y_col], s=15)
        else:
            ax.bar(df[x_col], df[y_col])
        ax.set_xlabel(x_col); ax.set_ylabel(y_col); ax.grid(True, alpha=0.3)
        st.pyplot(fig)

        # ダウンロード
        download_link_from_df(df, filename="uploaded.csv", label="このCSVデータを保存")
    else:
        st.info("サンプルデータを使用します。")
        df = pd.DataFrame({
            "x": np.arange(30),
            "y": np.random.randint(50, 150, 30)
        })
        st.dataframe(df.head())
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(df["x"], df["y"], ax.grid(True, alpha=0.3))
        st.pyplot(fig)


# ====== 2) 時系列(CSV) ======
elif page.startswith("2)"):
    st.subheader("時系列（CSV）")
    st.write("日付列を指定してインデックス化 → 折れ線・移動平均・月次集計")

    file = st.file_uploader("CSVを選択（例：date, value)", type=["csv"])
    date_col = st.text_input("日時列名（例：date）", value="date")
    val_col = st.text_input("値列名（例：value/ sales)", value="value")
    ma_window = st.slider("移動平均の窓", 3, 60, 7)

    if file is not None:
        df = pd.read_csv(file)
    else:
        st.info("サンプルデータを使用します。")
        df = pd.DataFrame({
            "date": pd.date_range("2025-07-01", periods=90, freq="D"),
            "value": np.random.randint(80, 200, 90)
        })
    
    try:
        ts = ensure_datetime_index(df, date_col)
        if val_col not in ts.columns:
            st.error(f"値列{val_col}が見つかりません。")
        else:
            # 折れ線グラフ + 移動平均
            fig, ax = plt.subplots(figsize=(9, 3.8))
            ts[val_col].plot(ax=ax, alpha=0.5, label="Daily")
            ts[val_col].rolling(ma_window).mean().plot(ax=ax, linewidth=2, label=f"{ma_window}-day MA")
            ax.legend(); ax.set_title("時系列データの折れ線と移動平均"); ax.grid(True, alpha=0.3)
            st.pyplot(fig)

            # 月次集計
            monthly = ts[val_col].resample("ME").sum()
            fig2, ax2 = plt.subplots(figsize=(9, 3))
            ax2.bar(monthly.index.strftime("%Y-%m"), monthly.values)
            ax2.set_title("月次合計"); ax2.set_xlabel("Month"); ax2.set_ylabel(val_col)
            st.pyplot(fig2)

    except Exception as e:
        st.exception(e)
