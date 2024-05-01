import socket
import sys

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(('0.0.0.0',10013))
s.listen(0)

while True:

    client, addr = s.accept()

    while True:
        data = client.recv(32)

        if len(data) == 0:
            break

        else:
            sys.stdout.write(data.decode())
            sys.stdout.flush()

client.close()