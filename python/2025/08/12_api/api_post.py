import requests

def post_api_date(url):
    """APIにPOSTリクエストを送信し、レスポンスを取得する関数"""
    try:
        payload = {
            "userId": 1,
            "id": 1,
            "title": "foo",
            "body": "bar"
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()  # HTTPエラーをチェック
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"APIリクエスト中にエラーが発生しました: {e}")
        return None

def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    data = post_api_date(url)
    if data:
        print("取得したデータ:")
        print(data)
    else:
        print("データの取得に失敗しました。")

if __name__ == "__main__":
    main()