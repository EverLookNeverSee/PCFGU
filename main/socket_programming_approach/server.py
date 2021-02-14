""" Fibonacci Microservice """

# import relevant modules
from socket import *


def fibonacci_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print(f"connection, {addr}")
        fib_handeler(client)
