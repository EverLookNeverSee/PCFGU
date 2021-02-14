""" Fibonacci Microservice """

# import relevant modules
from socket import *
from ..fib import fibonacci


def fibonacci_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print(f"connection, {addr}")
        fib_handler(client)


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        else:
            n = int(req)
            result = fibonacci(n)
            resp = str(result).encode("ascii") + b"\n"
            client.send(resp)
    print("closed")


# setting port
fibonacci_server(("", 25000))
