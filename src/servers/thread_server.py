import socket
import threading

DOMAIN = '0.0.0.0'
PORT = 8888

def handle_request(*args, **kwargs):
    pass

def threads():
    s = socket.socket()
    s.bind((DOMAIN, PORT))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        t = threading.Thread(target=handle_request, args=(cli))
        t.daemon = True
        t.start()

threads()
