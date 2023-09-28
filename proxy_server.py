import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "localhost"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        request = b''
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            request += data
        print(request)
        # tcp makes sure it is receive, udp does not
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_s:
            remote_host = socket.gethostbyname("www.google.com")
            client_s.connect((remote_host, 80))
            client_s.send(request)
            client_s.shutdown(socket.SHUT_WR)
            
            data = client_s.recv(BYTES_TO_READ)
            result = b'' + data
            while True:
                data = client_s.recv(BYTES_TO_READ)
                if not data:
                    break
                result += data
        print(result)
        conn.sendall(result)
        conn.close()
    
def multi_thread_server(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)
        
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

multi_thread_server(HOST, PORT)