from socket import socket, AF_INET, SOCK_STREAM

host = "127.0.0.1"
port = 65005

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect((host, port))
    while True:
        inputMessage = str(
            input("Write here an input message for socket server: "))
        sock.sendall(bytes(inputMessage, 'utf-8'))
        data = sock.recv(1024)

        print(f"Received {data}!!")
