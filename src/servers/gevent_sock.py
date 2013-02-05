import gevent
from gevent import socket
 
def handle_socket(sock):
    sock.sendall("HTTP/1.0 200 OK\r\nContent-Length: 5\r\n\r\nPong!\r\n")
    sock.close()
 
server = socket.socket()
server.bind(('0.0.0.0', 8888))
server.listen(500)
while True:
    try:
        new_sock, address = server.accept()
    except KeyboardInterrupt:
        break
    # handle every new connection with a new coroutine
    gevent.spawn(handle_socket, new_sock)
