import requests
import pandas as pd
from typing import Optional, Dict, Any, Union, List

def get_api_data(url: str,
                *,
                params: Optional[Dict[str, Any]] = None,
                timeout: float = 10.0,
            ) -> Optional[Union[Dict[str, Any], List[Dict[str, Any]]]]:
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"APIリクエスト中にエラーが発生しました: {e}")
        return None

def to_dataframe(data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> pd.DataFrame:
    """辞書 or 辞書のリストを DataFrame に変換"""
    if isinstance(data, list):
        return pd.DataFrame(data)
    else:
        return pd.DataFrame([data])

def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    data = get_api_data(url)
    if data:
        print("取得したデータ:")
        print(data)
    else:
        print("データの取得に失敗しました。")

    df = to_dataframe(data)
    print(pd)
    output_file = "api_data.csv"
    
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"データを {output_file} に保存しました。")

if __name__ == "__main__":
    main()