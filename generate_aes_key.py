# generate_aes_key.py
import os, base64, secrets
key = secrets.token_bytes(32)   # 32 bytes = 256 bits
print(base64.b64encode(key).decode())