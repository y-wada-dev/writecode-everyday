import json
import base64

def encode_json(data: dict) -> str:
    """"辞書データをBase64エンコードしてJSON形式で返す"""
    try:
        if "message" in data:
            data["message"] = base64.b64encode(
                data["message"].encode("utf-8")
            ).decode("utf-8")

        return json.dumps(data, ensure_ascii=False)
    
    except Exception as e:
        print("エンコードエラー:", e)
        return "{}"

def decode_json(json_str):
    """Base64含むJSON文字列をデコードして辞書形式で返す"""
    try:
        obj = json.loads(json_str)
        if "message" in obj:
            obj["message"] = base64.b64decode(obj["message"]).decode("utf-8")
        return obj
    
    except Exception as e:
        print("デコードエラー:", e)
        return {}

def main():

    data = {"name": "太郎", "message": "秘密のメッセージ"}

    json_str = encode_json(data)
    print("Base64入りJSON:", json_str)

    decoded = decode_json(json_str)
    print("復元後:", decoded)

if __name__ == "__main__":
    main()