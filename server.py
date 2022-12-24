import socket
import select

# Set a constant for the length of the header
HEADER_LENGTH = 10
# Define the IP and PORT to connect to
IP = "127.0.0.1"
PORT = 5000

# Create a socket object for the server using IPv4 and TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set the socket to reuse the address. This is useful for when the server is restarted and the port is still in use
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to the IP and PORT
serverSocket.bind((IP, PORT))
# Listen for connections
serverSocket.listen()

# Create a list of sockets to listen to. Add the server socket to the list
socketsList = [serverSocket]
# Create a dictionary to store the clients
clients = {}


def receiveMessage(clientSocket):
    try:
        # Receive the message header
        messageHeader = clientSocket.recv(HEADER_LENGTH)

        # Check to see if the message header is empty
        if not len(messageHeader):
            return False

        # Decode the message header from bytes to an integer
        messageLength = int(messageHeader.decode("utf-8"))

        # Return the message header and message
        return {"header": messageHeader, "data": clientSocket.recv(messageLength)}
    except:
        return False


while True:
    # Use select to listen to the sockets in the list
    readableSockets, _, exceptionSockets = select.select(socketsList, [], socketsList)

    # Loop through the sockets that are ready to be read
    for notifiedSocket in readableSockets:
        # Check to see if the socket is the server socket. This means a new connection has been made
        if notifiedSocket == serverSocket:
            # Accept the connection and store the client's socket object and address
            clientSocket, clientAddress = serverSocket.accept()

            # Receive the user's message
            user = receiveMessage(clientSocket)
            # Check to see if an error occurred
            if user is False:
                continue

            # Add the client's socket to the list of sockets to listen to
            socketsList.append(clientSocket)
            # Add the client's data to the dictionary of clients
            clients[clientSocket] = user

            # Print a message denoting the new connection
            print(
                f"Accepted new connection from {clientAddress[0]}:{clientAddress[1]} username: {user['data'].decode('utf-8')}"
            )
        else:
            # Receive the message from the client
            message = receiveMessage(notifiedSocket)

            # Check to see if an error occurred
            if message is False:
                print(
                    f"Closed connection from {clients[notifiedSocket]['data'].decode('utf-8')}"
                )
                # Remove the client's socket from the list of sockets to listen to
                socketsList.remove(notifiedSocket)
                # Remove the client's data from the dictionary of clients
                clients.pop(notifiedSocket)
                continue

            # Get the user from the dictionary of clients
            user = clients[notifiedSocket]
            # Print the user and message
            print(
                f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}"
            )

            # Loop through the clients and send the message that was received
            for clientSocket in clients:
                # Only relay the message to the client that didn't send the message
                if clientSocket != notifiedSocket:
                    clientSocket.send(
                        user["header"]
                        + user["data"]
                        + message["header"]
                        + message["data"]
                    )

    # Loop through the sockets that have an error
    for notifiedSocket in exceptionSockets:
        # Remove the client's socket from the list of sockets to listen to
        socketsList.remove(notifiedSocket)
        # Remove the client's data from the dictionary of clients
        clients.pop(notifiedSocket)
