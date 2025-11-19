import json

def read_json_from_string(json_str: str):

    data = json.loads(json_str)
    print(f"Data read from string: {data}")
    return data

def write_json_to_file(data, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data written to {filename}")

json_data = '{"name": "太郎", "age": 25}'

read_json_from_string(json_data)
write_json_to_file(read_json_from_string(json_data), "output.json")

