import csv

def read_csv(read_file_path):
    """CSVファイルを読み込む関数"""
    try:
        with open(read_file_path, mode= 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        return []
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {read_file_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def write_csv(write_csv_path, data):
    """CSVファイルにデータを書き込む関数"""
    try:
        with open(write_csv_path, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
        print(f"データを {write_csv_path} に書き込みました。")
    except PermissionError:
        print(f"書き込み権限がありません: {write_csv_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def main():
    # 読み込み用のCSVファイルパス
    read_file_path = 'sample.csv'

    # 書き込み用のCSVファイルパス
    write_csv_path = 'output.csv'

    # 書き込みデータ
    data = [
        ["名前", "年齢", "職業"],
        ["tanaka", 25, "エンジニア"],
        ["sato", 30, "デザイナー"],
        ["suzuki", 22, "マネージャー"]
    ]
    
    # 読み込み
    print("CSVファイルの読み込み:")
    original_data = read_csv(read_file_path)
    if original_data:
        print("読み込んだデータ:")
        for row in original_data:
            print(row)

    # 書き込み
    print("\nCSVファイルへの書き込み:")
    write_csv(write_csv_path, data)
    print(f"{write_csv_path} にデータを書き込みました。")

    # 再度読み込み確認
    print("\n書き込んだCSVファイルの内容:")
    new_data = read_csv(write_csv_path)
    if new_data:
        print("書き込んだデータ:")
        for row in new_data:
            print(row)
            
if __name__ == "__main__":
    main()


