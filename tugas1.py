import socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 10013))
s.listen(0)

while True:

    client, addr = s.accept()

    data = "200"
    #kirim data
    client.send(data.encode())

    client.close()