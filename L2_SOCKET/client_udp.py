from socket import *

from requests import Response

server_name = "localhost"
server_port = 12000
# Apertura socket
client_Socket = socket(AF_INET, SOCK_DGRAM)
# Messaggio al server
message = input("Inserire testo: ")
# Inviamo il messaggio
server_address = (server_name, server_port)
# Encoding
message = message.encode("utf-8")
client_Socket.sendto(message, server_address)
# Ricezione risposta
response, server_info = client_Socket.recvfrom(1024)
# Deocde risposta
response = response.decode("utf-8")
print(f"Risposta server: {response}")
# Chiusura socket
client_Socket.close()
