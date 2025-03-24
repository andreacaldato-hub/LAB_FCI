from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to the server's address
server_socket.bind(("", server_port))
print("The server is ready to receive")

vocali = ["a", "e", "i", "o", "u"]

while True:
    # Receive message from client
    message, client_address = server_socket.recvfrom(2048)
    print(f"Received message from {client_address}")

    # Decode the message
    message_mod = message.decode("utf-8").lower()

    # Count vowels and consonants
    vocali_count = sum(1 for char in message_mod if char in vocali)
    consonanti_count = sum(
        1 for char in message_mod if char.isalpha() and char not in vocali
    )

    # Convert consonant count to string and encode
    consonanti_count_str = str(consonanti_count).encode("utf-8")

    # Send response to the client
    server_socket.sendto(consonanti_count_str, client_address)
    print(f"Sent consonant count: {consonanti_count}")
