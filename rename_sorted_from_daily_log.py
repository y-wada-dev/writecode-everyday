# rename_sorted_from_daily_log.py
import os
from collections import OrderedDict

ROOT = os.path.dirname(os.path.abspath(__file__))
DAILY_LOG = os.path.join(ROOT, "docs", "daily-log.md")
SORTED_ROOT = os.path.join(ROOT, "python", "sorted")

def parse_daily_log():
    """
    docs/daily-log.md から
    old_dir_name -> new_dir_name(YYYYMMDD_slug)
    の対応を作る
    """
    mapping = OrderedDict()  # 先に出てきたもの優先
    with open(DAILY_LOG, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("| 2025-"):
                continue  # ヘッダなどは飛ばす

            # | Date | What | Path | Tags |
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) < 3:
                continue
            date_str, what, path = cols[0], cols[1], cols[2]

            # Path が python/ から始まらない場合はスキップ
            if not path.startswith("python/"):
                continue

            # 既に YYYYMMDD_ 形式のディレクトリならスキップ（例: python/20250808_monte/）
            dir_name = os.path.basename(os.path.dirname(path))
            if dir_name.startswith("2025"):
                continue

            # 日付を YYYYMMDD に
            yyyymmdd = date_str.replace("-", "")  # "2025-08-08" -> "20250808"

            # dir_name は "08_monte" みたいな想定
            # "_" 以降をスラッグとして使う
            if "_" in dir_name:
                _, slug = dir_name.split("_", 1)
            else:
                slug = dir_name

            new_dir_name = f"{yyyymmdd}_{slug}"

            # 最初に見つけた対応だけ採用（後の重複は無視）
            if dir_name not in mapping:
                mapping[dir_name] = new_dir_name

    return mapping


def find_and_rename_sorted(mapping, dry_run=True):
    """
    python/sorted 以下を走査して、
    mapping にあるディレクトリ名を YYYYMMDD_slug にリネーム
    """
    for category in os.listdir(SORTED_ROOT):
        category_path = os.path.join(SORTED_ROOT, category)
        if not os.path.isdir(category_path):
            continue

        for old_dir, new_dir in mapping.items():
            old_path = os.path.join(category_path, old_dir)
            new_path = os.path.join(category_path, new_dir)

            if os.path.isdir(old_path):
                if dry_run:
                    print(f"[DRY-RUN] {old_path} -> {new_path}")
                else:
                    print(f"RENME: {old_path} -> {new_path}")
                    os.rename(old_path, new_path)


if __name__ == "__main__":
    mapping = parse_daily_log()
    print("# Mapping (old_dir -> new_dir)")
    for k, v in mapping.items():
        print(f"{k} -> {v}")

    print("\n# Searching and renaming in python/sorted (dry-run)")
    find_and_rename_sorted(mapping, dry_run=True)

    print("\n# 実行したいときは dry_run=False にして再実行してください。")
