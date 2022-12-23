import socket
import time
import pickle

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
    dictionary = {1: "Hey", 2: "There"}
    # Encode the dictionary to bytes and create the message
    message = pickle.dumps(dictionary)
    message = bytes(f"{len(message):<{HEADERSIZE}}", "utf-8") + message

    # Send the message to the client
    clientsocket.send(message)
