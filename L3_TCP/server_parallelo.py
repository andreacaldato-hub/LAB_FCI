from socket import *
import threading


def client_handler(connection_socket):
    while True:
        richiesta = connection_socket.recv(2048)

        if richiesta.decode == ".":
            print("Sconnetto il client")
            connection_socket.close()
            break
    connection_socket.send(richiesta.decode.upper())


sever_port = 12000
welcome_socket = socket(AF_INET, SOCK_STREAM)
# bind della socket alla porta 12000
welcome_socket.bind(("localhost", sever_port))
# definisco la coda dei client
welcome_socket.listen(1)  # 1 = max 3 client
print("Server pronto")
while True:
    connection_socket, client_address = welcome_socket.accept()
    print(f"Client {client_address} connesso")
    thread = threading.Thread(target=client_handler, args=(connection_socket,))
    thread.start()
