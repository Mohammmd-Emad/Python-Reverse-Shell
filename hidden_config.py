import base64

def encode_config(ip_port: str, key: int = 0x4B):
    # Encode to bytes
    data = ip_port.encode('utf-8')
    # First Base64
    b64_1 = base64.b64encode(data)
    # XOR
    xored = bytes(b ^ key for b in b64_1)
    # second Base64
    final = base64.b64encode(xored)
    return final.decode('utf-8')

print(encode_config("192.168.1.28:7777"))
