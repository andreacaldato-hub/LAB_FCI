from socket import *

sever_port = 12000
welcome_socket = socket(AF_INET, SOCK_STREAM)
# bind della socket alla porta 12000
welcome_socket.bind(("", sever_port))
# definisco la coda dei client
welcome_socket.listen(1)
print("Server pronto")
while True:
    print("Server in ascolto")
    # blocco finche non ho comunicazione con un client
    connection_socket, client_address = welcome_socket.accept()
    print(f"Il client si 'e connesso: {client_address} ")
    # leggo la stringa dal client
    richiesta = connection_socket.recv(2048)
    richiesta_decoded = richiesta.decode("utf-8")
    print(f"Ho ricevuto il messaggio: {richiesta_decoded}")
    modified_message = richiesta_decoded.upper()
    # mando il messaggio encoded
    connection_socket.send(modified_message.encode())
    print("Ho inviato il messaggio al client")
    connection_socket.close()
