from socket import *
def is_Prime(richiesta_decoded):
    print("ciao")


sever_port = 12000
welcome_socket = socket(AF_INET, SOCK_STREAM)
# bind della socket alla porta 12000
welcome_socket.bind(("localhost", sever_port))
# definisco la coda dei client
welcome_socket.listen(1)  # 1 = max 3 client
print("Server pronto")
while True:
    print("Server in ascolto")
    # blocco finche non ho comunicazione con un client
    connection_socket, client_address = welcome_socket.accept()
    print(f"Il client si 'e connesso: {client_address} ")
    while True:
        # leggo la stringa dal client
        richiesta = connection_socket.recv(2048)
        richiesta_decoded = richiesta.decode("utf-8")
        print(f"Ho ricevuto il messaggio: {richiesta_decoded}")
        if richiesta_decoded == "exit":
            print(f"Chiusura della socket del client {client_address}")
            connection_socket.close()
            break
        if is_Prime == True
        # mando il messaggio encoded
        str = "Il numero é primo"
        connection_socket.send(str.encode())
        print(f"Ho inviato il messaggio al client {client_address}")
