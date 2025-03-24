from socket import *

from requests import Timeout


server_name = "localhost"
server_port = 12000
# Apertura socket
client_Socket = socket(AF_INET, SOCK_DGRAM)
# Timeout
client_Socket.settimeout(5)
# Messaggio al server
message = input("Inserire testo: ")
# Inviamo il messaggio
server_address = (server_name, server_port)
# Encoding
message = message.encode("utf-8")
client_Socket.sendto(message, server_address)
# Prova a fare queste operazioni a meno di eccezzioni
try:
    response, server_info = client_Socket.recvfrom(1024)
    print(f"Risposta ricevuto: {response.decode('utf-8')}")
# In caso di errori
except:
    print("Errore generico")
except timeout:
    print("Timeout scaduto, server non raggiungibile")
finally:
    client_Socket.close()
