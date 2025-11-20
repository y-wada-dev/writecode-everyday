from __future__ import annotations
import json
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any, Dict

# ログ出力設定
LOG_DIR = Path("./logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "error.log"

logger = logging.getLogger("practice")
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(
    LOG_FILE, maxBytes=200_000, backupCount=3, encoding="utf-8"
)

file_handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
))

logger.addHandler(file_handler)

# logger.exception("エラーメッセージ")

# エラーの発生を確認するための関数
def divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("0で割ろうとしたためエラーが発生しました")
        raise
    except TypeError as e:
        logger.exception("数値以外のためエラーが発生しました")
        raise

def parse_int(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        logger.exception(f"'{text}'は整数に変換できませんでした")
        return 0
    
def read_text(path: Path) -> str:
    try:
        with path.open(encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logger.exception(f"ファイルが見つかりません: {path}")
        return ""
    except PermissionError:
        logger.exception(f"ファイルの読み取り権限がありません: {path}")
        raise

def get_key(d: Dict[str, Any], key: str) -> Any:
    try:
        return d[key]
    except KeyError:
        logger.exception(f"`キーが存在しません: {key!r} in {d}")
        return None

def get_index(seq: list[Any], idx={int}) -> Any:
    try:
        return seq[idx]
    except IndexError:
        logger.exception(f"範囲外アクセス: idx={idx}, len={len(seq)}")
        return seq[-1] if seq else None

def parse_json(text: str) -> Dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        logger.exception("JSONの解析に失敗しました")
        return {}

def write_then_read(path: Path, text: str) -> str:
    f = None
    try:
        f = path.open("w", encoding="utf-8")
        f.write(text)
    except OSError:
        logger.exception(f"ファイルの書き込みに失敗しました: {path}")
        return ""
    else:
        logger.info(f"ファイルに書き込みました: {path}")
        return path.read_text(encoding="utf-8")
    finally:
        if f and not f.closed:
            f.close()

class NegativePriceError(ValueError):
    pass

def calc_toal(price: float, qtr: int) -> float:
    if price < 0:
        logger.exception(f"価格の値が負です: price={price}")
        raise NegativePriceError("価格は0円以上でなければなりません")
    if qtr < 0:
        logger.exception(f"数量の値が負です: qtr={qtr}")
        raise ValueError("数量は0以上でなければなりません")
    return price * qtr

def main() -> None:
    print("=== Error Handling Practice ===")

    try:
        print("divide(10, 2) =", divide(10, 2))
        print("divide(10, 0) =", divide(10, 0))
    except Exception as e:
        print("divideで例外発生:", e)
    
    print("parse_int('123') =", parse_int("123"))
    print("parse_int('abc') =", parse_int("abc"))

    print("read_text('no_such_file.text') =", read_text(Path("no_such_file.txt"))[:20])

    print("get_key({'a': 1}, 'b') =", get_key({'a': 1}, 'b'))
    print("get_index([10, 20], 5) =", get_index([10, 20], 5))

    ok = parse_json('{a:1}')
    ng = parse_json('{"a":1,,}')
    print("parse_json ok =", ok, "ng =", ng)

    tmp = Path("tmp.txt")
    print("write_then_read =", write_then_read(tmp, "こんにちは"))

    try:
        tmp.unlink()
    except FileNotFoundError:
        pass

    try:
        print("calc_total =", calc_toal(120.0, 3))
        print("calc_total NG =", calc_toal(-120.0, 1))
    except NegativePriceError as e:
        print("NegativePriceError:", e)

if __name__ == "__main__":
    main()
    print(f"\n→ エラーログは {LOG_FILE} に出力されます")