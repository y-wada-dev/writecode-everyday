from __future__ import annotations
import os
from pathlib import Path
import shutil
from datetime import datetime

"""
ファイル・ディレクトリ操作の基本
os モジュール
    os.getcwd() 現在の作業ディレクトリ取得
    os.listdir() ファイル一覧取得
    os.mkdir() / os.makedirs() フォルダ作成
    os.rename() 名前変更
    os.remove() ファイル削除

pathlib モジュール
    Path クラスを使ったパス操作
    Path.exists() / Path.is_file() / Path.is_dir()
"""


# def file_handling_example():
#     with open("sample.text", "w", encoding="utf-8") as f:
#         f.write("Hello, World!")


#　設定値定義
ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
TXT_NAME = "sample.txt"
DATE_DIR = ROOT / datetime.now().strftime("%Y%m%d_file_backup")

def ensure_dir(path: Path):
    """ディレクトリの準備"""
    try:
        path.mkdir(parents= True, exist_ok=True)
        print(f"ディレクトリ {path} を作成しました")
    except FileExistsError:
        print(f"ディレクトリ {path} はすでに存在します")

def write_text_file(path: Path, text:str, encoding: str = "utf-8") -> None:
    """テキストファイルへの書き込み"""
    try:
        path.parent.mkdir(parents=True,exist_ok=True)
        with open(path, "w", encoding=encoding, newline="") as f:
            f.write(text)
        print(f"ファイルに書き込みました：{path}")
    except Exception as e:
        print(f"ファイル書き込みエラー {path} : {e}")
        raise

def read_text_file(path: Path) -> list[Path]:
    """ファイル一覧の取得"""
    try:
        if not path.exists():
            raise FileNotFoundError(f"ファイルが存在しません: {path}")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"ファイルを読み込みました: {path}")
        return content
    except Exception as e:
        print(f"[ERROR] ファイル一覧取得エラー {path} : {e}")
        raise

def list_files(dir_path: Path) -> list[Path]:
    """ディレクトリ内のファイル一覧を取得"""
    try:
        if not dir_path.exists():
            print(f"[WARN] ディレクトリが存在しません: {dir_path}")
            return []
        files = [p for p in dir_path.iterdir() if p.is_file()]
        print(f"[OK] ファイル一覧を取得しました: {len(files)} 件")
        return files
    except Exception as e:
        print(f"[ERROR] ファイル一覧取得エラー {dir_path} : {e}")
        raise

def find_by_extension(dir_path: Path, ext: str) -> list[Path]:
    """ファイル検索"""
    if not ext.startswith("."):
        ext = "." + ext
    try:
        files = [p for p in dir_path.rglob(f"*{ext}") if p.is_file()]
        print(f"[OK] 拡張子 {ext} のファイルを検索しました: {len(files)} 件")
        return files
    except Exception as e:
        print(f"[ERROR] ファイル検索エラー {dir_path}, ext={ext} : {e}")
        raise

def move_file(paths: list[Path], dest_dir: Path) -> None:
    """ファイル移動"""
    ensure_dir(dest_dir)
    moved = 0
    for p in paths:
        try:
            target = dest_dir / p.name

            if target.exists():
                stem = target.stem
                suffix = target.suffix
                counter = 1
                while True:
                    new_name = f"{stem}_{counter}{suffix}"
                    new_target = dest_dir / new_name
                    if not new_target.exists():
                        target = new_target
                        break
                    counter += 1

            shutil.move(str(p), str(target))
            moved += 1
            print(f"[OK] ファイルを移動しました: {p} → {target}")

        except Exception as e:
            print(f"[ERROR] ファイル移動エラー {p} → {dest_dir} : {e}")

    print(f"[OK] {moved} 件のファイルを移動しました")

def main():
    """メイン処理"""
    # file_handling_example()

    print("===ディレクトリ準備===")
    ensure_dir(DATA_DIR)

    print("===テキストファイル書き込み===")
    file_path = DATA_DIR / TXT_NAME
    write_text_file(file_path, "Hello, World!\n練習用のテキストファイルです。")
    content = read_text_file(file_path)
    print("---読み込み内容---")
    print(content.strip())

    print("===ファイル一覧取得===")
    files = list_files(DATA_DIR)
    for p in files:
        print(f" - {p.name}")

    print("===拡張子でファイル検索 (.txt) ===")
    txt_files = find_by_extension(DATA_DIR, ".txt")
    for p in txt_files:
        print(" *", p)

    print("===ファイル移動===")
    move_file(txt_files, DATE_DIR)

    print("===ファイル移動後の一覧===")
    print("data/ の残りファイル:", [p.name for p in list_files(DATA_DIR)])
    print("date_dir の中:", [p.name for p in list_files(DATE_DIR)])
    print("===処理完了===")

if __name__ == "__main__":
    main()