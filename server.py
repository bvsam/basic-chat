import socket
import time

# Set a constant for the length of the header
HEADERSIZE = 10

# Create a socket object for the server using IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the host and port 5000
s.bind((socket.gethostname(), 5000))
# Listen for connections with a queue of 5
s.listen(5)

while True:
    # Accept a connection and store the client's socket object and address
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    # Create a message with a fixed length header of HEADERSIZE containing the length of the message and the message itself
    message = "Welcome to the server!"
    message = f"{len(message):<{HEADERSIZE}}{message}"

    # Send the message to the client
    clientsocket.send(bytes(message, "utf-8"))

    while True:
        time.sleep(3)
        message = f"The time is {time.time()}"
        message = f"{len(message):<{HEADERSIZE}}{message}"
        clientsocket.send(bytes(message, "utf-8"))
