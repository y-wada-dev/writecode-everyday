import base64

# 元のテキスト
original_text = "hello world"
print(f"Original text: {original_text}")

# Base64エンコード
encode_bytes = base64.b64encode(original_text.encode('utf-8'))
encode_text = encode_bytes.decode('utf-8')
print(f"Encoded text: {encode_text}")

# Base64デコード
decode_bytes = base64.b64decode(encode_bytes)
decode_text = decode_bytes.decode('utf-8')
print(f"Decoded text: {decode_text}")
