import socket
from time import sleep
from datetime import date, datetime

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 56000  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"{datetime.now()} - no data available...")
            else: print(f"{datetime.now()} - {data}")
            sleep(30)