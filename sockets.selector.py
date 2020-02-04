import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP/IP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # asocket layer, reuse addr without timeout
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept)


def accept(server_sock: socket):
    client_socket, addr = server_sock.accept()
    print('connection from: ', addr)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_msg)


def send_msg(client_sock: socket):
    request = client_sock.recv(4096)
    if request:
        response = 'server: I got msg "{}"\n'.format(request[:-1].decode())  # [:-1] - cut newline
        client_sock.send(response.encode())
    else:
        selector.unregister(client_sock)
        client_sock.close()


def event_loop():
    while True:
        events = selector.select()  # (key, events)
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


def main():
    server()
    event_loop()


if __name__ == '__main__':
    main()
