import socket

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
    # Send a message to the client
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    # Close the connection
    clientsocket.close()