import os
import shutil
import re

ROOT = "./2025"
SORTED_ROOT = "./sorted"

# ① 明示的にカテゴリを決めたいフォルダ（例：今回の2つ）
EXPLICIT_MAP = {
    "01~08_evaluating_classification_models": "data_science_ml",
    "25~30_scraping": "data_engineering",
    "01_k-means": "data_science_ml",
    "07~20_app.py": "data_science_ml",
    "15~16_temp_data": "visualization_geospatial",
    "17~18_temp_plot": "visualization_geospatial",
}

# ② キーワードベースのカテゴリマップ（単語単位でマッチさせる）
CATEGORIES = {
    "basic_python": [
        "monte", "multiplication", "typing", "sort",
        "class", "file", "error", "list", "text", "even", "count"
    ],
    "csv_json_handling": ["pandas", "csv", "json", "base64"],
    "api_http": ["api"],
    "algorithms_data_structures": ["tree", "heap"],
    "visualization_matplotlib": [
        "matplotlib", "scatter", "regression", "time",
        "pie", "histgram", "weather", "boxplot", "heatmap"
    ],
    "visualization_geospatial": [
        "choropleth", "japan", "pref", "temp_heatmap"
    ],
    "data_science_ml": [
        "k-means", "nlp", "cleaning", "missing",
        "outlier", "winsor", "scaler", "feature",
        "correlation", "regression_models",
        "classification_models"
    ],
    "data_engineering": [
        "scrape", "scraping", "sqlite", "cleaned"
    ],
}


def split_tokens(name: str):
    """フォルダ名を単語っぽく分割して小文字のリストにする"""
    # 数字・記号で分割
    tokens = re.split(r"[^a-zA-Z0-9]+", name.lower())
    return [t for t in tokens if t]


def find_category(folder_name: str) -> str:
    # ① まずは EXPLICIT_MAP を見る（今回の2件みたいなやつ）
    if folder_name in EXPLICIT_MAP:
        return EXPLICIT_MAP[folder_name]

    tokens = split_tokens(folder_name)

    # ② 単語単位でマッチ
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            kw_low = kw.lower()
            # 完全一致 or tokenに含まれる形で判定
            if kw_low in tokens:
                return category
            # "k-means" みたいなものは部分一致も許容
            if any(kw_low in t for t in tokens):
                return category

    return "others"


def main():
    os.makedirs(SORTED_ROOT, exist_ok=True)

    for month in os.listdir(ROOT):
        ym_path = os.path.join(ROOT, month)
        if not os.path.isdir(ym_path):
            continue

        for folder in os.listdir(ym_path):
            fpath = os.path.join(ym_path, folder)
            if not os.path.isdir(fpath):
                continue

            category = find_category(folder)
            dest = os.path.join(SORTED_ROOT, category)
            os.makedirs(dest, exist_ok=True)

            shutil.copytree(fpath, os.path.join(dest, folder), dirs_exist_ok=True)

            print(f"{folder:40} → {category}")


if __name__ == "__main__":
    main()
