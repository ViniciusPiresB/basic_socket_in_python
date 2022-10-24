from socket import socket, AF_INET, SOCK_STREAM

host = "127.0.0.1"
port = 65005

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    connection, addr = sock.accept()
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            data = str(data).replace("b'", "")[:-1]
            print(data)
            connection.sendall(bytes(data, 'utf-8'))
