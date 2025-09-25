import time
import re
import math
import sqlite3
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE = "https://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0 (practice; +https://example.com)"}
OUT_CSV = Path("books_scraped.csv")
OUT_DB  = Path("books.db")

# カテゴリ
CATEGORY_URL = urljoin(BASE, "catalogue/category/books/science-fiction_16/index.html")

# ★評価の語→数値
RATING_MAP = {
    "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# --HTTP ヘルパ（リトライ付き）
def fetch_url(url:str, session: requests.Session, max_retry=3, backoff=1.5) -> str:
    for i in range(max_retry):
        try:
            r = session.get(url, headers=HEADERS, timeout=15)
            r.raise_for_status()
            r.encoding = "utf-8"
            return r.text
        except requests.RequestException as e:
            if i == max_retry - 1:
                raise
            time.sleep(backoff ** i)