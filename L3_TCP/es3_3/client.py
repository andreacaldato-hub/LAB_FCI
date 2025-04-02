from socket import *
import threading


def timeout_reached():
    print("Timeout reached at 10 seconds!")


# Start a timer that runs `timeout_reached` after 10 seconds

server_name = "localhost"
server_port = 12000
# apro la socket
client_socket = socket(AF_INET, SOCK_STREAM)
print("Provo a connettermi")
client_socket.connect((server_name, server_port))
while True:
    # chiedo all'utente una stringa
    messsage = input("Inserisci un numero o 'exit' per terminare: ")
    # encode message
    encoded_message = messsage.encode("utf-8")
    # invio il messaggio encoded
    client_socket.send(encoded_message)
    if messsage == "exit":
        print("Chiusura della socket")
        client_socket.close()
        break
    # ricevo la risposta dal server
    risposta = client_socket.recv(2048)
    print(f"Il server ha risposto: {risposta.decode()}")
