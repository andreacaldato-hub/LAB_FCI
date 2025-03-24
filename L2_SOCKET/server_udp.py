from socket import *

server_port = 12001
server_socket = socket(AF_INET, SOCK_DGRAM)
# Binding della socket all'indirizzo del server
server_socket.bind(("", server_port))
print("The server is ready to receive")
# Ciclo infinito di ricezione dei pacchetti
while True:
    # Ricezione del messaggio dal client
    message, client_address = server_socket.recvfrom(2048)
    # Decodifica del messaggio
    print(f"Ricevuto messaggio da {client_address}")
    message = message.decode("utf-8")
    # Elaborazione del messaggio (maiuscolo)
    modified_message = message.upper()
    # Mandiamo risposta al client
    server_socket.sendto(modified_message.encode("utf-8"), client_address)
