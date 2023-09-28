import socket


BYTES_TO_READ = 4096
HOST = "localhost"
PORT = 8001

def server(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.listen(2)    
            while True:
                conn, addr = s.accept() # conn is socket referring to client
                data = conn.recv(BYTES_TO_READ)
                print(data)
                if not data:
                    break
                conn.sendall(data)
                conn.close()
server(HOST, PORT)