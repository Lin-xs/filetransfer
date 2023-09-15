
import os
import socket
from tqdm import tqdm

# IP = socket.gethostbyname(socket.gethostname())
IP = '162.105.146.175'
PORT = 4456
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
FILENAME = "friends-final.txt"
FILENAME = "/Users/yuanqingwang/opt-125m.tar.gz"
FILESIZE = os.path.getsize(FILENAME)

def main():
    """ TCP socket and connecting to the server """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    """ Sending the filename and filesize to the server. """
    data = f"{FILENAME}*{FILESIZE}"
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"SERVER: {msg}")

    """ Data transfer. """
    bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(FILENAME, "rb") as f:
        while True:
            data = f.read(SIZE)

            if not data:
                break

            # client.send(data.encode(FORMAT))
            client.send(data)
            # msg = client.recv(SIZE).decode(FORMAT)

            bar.update(len(data))

    """ Closing the connection """
    client.close()

if __name__ == "__main__":
    main()

