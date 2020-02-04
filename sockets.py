import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # args: IPv4, TCP/IP
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # args: socket layer, reuse addr without timeout
serverSocket.bind(('localhost', 5000))
serverSocket.listen()


def server():
    while True:  # outer loop: waiting connections from clients on server
        client_tuple = serverSocket.accept()
        print('connection from: ', client_tuple[1])
        client(client_tuple)


def client(tupl):
    addr = tupl[1]
    sock = tupl[0]
    while True:  # inner loop: waiting requests(messages) from client in connection
        request = sock.recv(4096)
        if request:
            response = 'server: I got msg "{}" from {} \n'.format(request[:-1].decode(), addr[1])  # [:-1] - cut newline
            print('client {}: '.format(addr[1]), request)
            sock.send(response.encode())
        else:
            break


server()
