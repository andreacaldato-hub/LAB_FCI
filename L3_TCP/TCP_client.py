from socket import *

server_name = "localhost"
server_port = 12000
# apro la socket
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
# chiedo all'utente una stringa
messsage = input("Inserisci un messagioci: ")
# encode message
encoded_message = messsage.encode("utf-8")
# invio il messaggio encoded
client_socket.send(encoded_message)

# ricevo la risposta dal server
risposta = client_socket.recv(2048)
print(f"Il server ha risposto: {risposta.decode()}")
client_socket.close()
