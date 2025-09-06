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

