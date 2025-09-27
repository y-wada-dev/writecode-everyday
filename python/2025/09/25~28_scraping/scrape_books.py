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
def fetch_html(url:str, session: requests.Session, max_retry=3, backoff=1.5) -> str:
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

# --1ページ分の書籍データを抽出
def parse_list_page(html: str, page_url: str):
    soup = BeautifulSoup(html, "lxml")
    items = []
    for art in soup.select("article.product_pod"):

        title = art.h3.a.get("title", "").strip()

        price_text = art.select_one("p.price_color").get_text(strip=True)
        price = float(re.sub(r"[^\d.]", "", price_text))

        rating_cls = art.select_one(".start-rating")
        rating = None

        if rating_cls:
            for c in rating_cls.get("class", []):
                if c in RATING_MAP:
                    rating = RATING_MAP[c]
        
        # 詳細ページURL
        rel = art.h3.a.get("href", "")
        product_url = urljoin(page_url, rel)

        items.append({
            "title": title,
            "price_gbp": price,
            "rating": rating,
            "stock_text": stock,
            "product_url": product_url
        })

    next_link = soup.select_one("li.next > a")
    next_url = urljoin(page_url, next_link["href"]) if next_link else None
    return items, next_url

# 全ページを巡回してデータ収集
def crawl_category(start_url: str, delay_sec=1.0, max_pages=100):
    all_rows = []
    url = start_url
    with requests.Session() as sess:
        pages = 0
        while url and pages < max_pages:
            html = fetch_html(url, sess)
            rows, next_url = parse_list_page(html, url)
            all_rows.extend(rows)
            pages += 1
            print(f"[OK] {url} -> {len(rows)}件 (累計{len(all_rows)}件)")
            url = next_url
            time.sleep(delay_sec)
    return all_rows

# ---保存（CSV / SQLite）
