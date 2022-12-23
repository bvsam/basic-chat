import socket
import pickle

# Set a constant for the length of the header
HEADERSIZE = 10

# Create a socket object for the client using IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
s.connect((socket.gethostname(), 5000))

while True:
    # Create an empty string to store the full message
    fullMessage = b""
    newMessage = True

    while True:
        # Receive a message from the server, with a buffer size of 16 bytes
        message = s.recv(16)

        # Check to see if the message is new
        if newMessage:
            # Get the length of the message from the header
            msgLength = int(message[:HEADERSIZE])
            print(f"New message length: {msgLength}")
            # Set newMessage to False to indicate that the first message has been received
            newMessage = False

        # Decode the message from bytes to a string and add it to the full message
        fullMessage += message

        # Check to see if the full message has been received
        if len(fullMessage) - HEADERSIZE == msgLength:
            print("Full message received")
            print(fullMessage[HEADERSIZE:])

            # Decode the full message from bytes to a string and print it
            dictionary = pickle.loads(fullMessage[HEADERSIZE:])
            print(dictionary)

            # Set newMessage to True to set up for the next message
            newMessage = True
            # Reset the full message
            fullMessage = b""

    print(fullMessage)
