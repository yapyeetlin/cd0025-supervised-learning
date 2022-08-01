import socket
import os
from time import sleep

HOST = "localhost"  # The server's hostname or IP address
PORT = 56000  # The port used by the server
WAIT = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    while True:
        print(f"Attempt connection to {HOST}...")

        try:
            s.connect((HOST, PORT))
            s.send(b"Hello, world")
            sleep(1)
            s.close()
            
        except KeyboardInterrupt:
            exit()
            
        except:
            print(f"Connection to {HOST} failed...")
            for int in range(WAIT, 0, -1):
                print(f"Restart in {int} seconds...")
                sleep(1)
            os.system("cls")
            continue

