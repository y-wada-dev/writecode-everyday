import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

BASE = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (practice; +https://example.com)" 
}

def fetch(url: str) -> str:
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    r.encoding = "utf-8"
    return r.text

def parse_book_list(html: str):
    soup = BeautifulSoup(html, "lxml")  # or "html.parser"
    items = []
    for art in soup.select("article.product_pod"):
        title = art.h3.a["title"]
        price_text = art.select_one(".price_color").get_text(strip=True)
        # ★数字だけ抽出して float に
        price_val = float(re.sub(r"[^\d.]", "", price_text))
        rating = art.select_one(".star-rating")["class"][1]  # "Three" など
        items.append({"title": title, "price_gbp": price_val, "rating": rating})
    return items

def main():
    all_rows = []
    for path in ["index.html", "catalogue/page-2.html"]:
        html = fetch(BASE + path)
        all_rows.extend(parse_book_list(html))

    df = pd.DataFrame(all_rows)
    print(df.head())

    df.to_csv("book.csv", index=False, encoding="utf-8-sig")

    ax = df["price_gbp"].plot(kind="hist", bins=20, figsize=(6, 4))
    ax.set_title("Book price Distribution")
    ax.set_xlabel("Price (GBP)")
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()