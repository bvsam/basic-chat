import socket
import select
import errno
import sys

# Set a constant for the length of the header
HEADER_LENGTH = 10
# Define the IP and PORT to connect to
IP = "127.0.0.1"
PORT = 5000

# Get the client's username
myUsername = input("Username: ")
# Create a socket object for the client using IPv4 and TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
clientSocket.connect((IP, PORT))
# Set the socket to non-blocking mode. This means that the socket will not wait for data to be received
clientSocket.setblocking(False)

# Create a header for the username and send it to the server
myUsernameHeader = f"{len(myUsername):<{HEADER_LENGTH}}"
clientSocket.send(f"{myUsernameHeader}{myUsername}".encode("utf-8"))

while True:
    # Get the message from the user
    message = input(f"{myUsername} > ")

    # Check to see if the message is not empty
    if message:
        # Create a header for the message and send it to the server
        messageHeader = f"{len(message):<{HEADER_LENGTH}}"
        clientSocket.send(f"{messageHeader}{message}".encode("utf-8"))

    try:
        while True:
            # Receive the username header of the new message from the server
            usernameHeader = clientSocket.recv(HEADER_LENGTH)

            # Check to see if the username header is empty
            if not len(usernameHeader):
                print("Connection closed by the server")
                sys.exit()

            # Get the length of the username from the header and receive the username
            usernameLength = int(usernameHeader.decode("utf-8"))
            username = clientSocket.recv(usernameLength).decode("utf-8")

            # Receive the message header of the new message from the server
            messageHeader = clientSocket.recv(HEADER_LENGTH)
            messageLength = int(messageHeader.decode("utf-8"))
            # Receive the message from the server
            message = clientSocket.recv(messageLength).decode("utf-8")

            # Print the message
            print(f"{username} > {message}")

    except IOError as e:
        # Check to see if the error is NOT due to no data being received. If so, print the error and exit the
        # program. If no data was received, this will cause an error which will be caught and ignored
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print(f"Reading error: {str(e)}")
            sys.exit()
    except Exception as e:
        # If any other error occurs, print the error and exit the program
        print(f"General error: {e}")
        sys.exit()
