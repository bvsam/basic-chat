import socket

# Create a socket object for the client using IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
s.connect((socket.gethostname(), 5000))

# Create an empty string to store the full message
full_msg = ""

while True:
    # Receive a message from the server, with a buffer size of 1024 bytes
    msg = s.recv(1024)
    # If the message is empty, break out of the loop
    if len(msg) <= 0:
        break
    # Decode the message from bytes to a string and add it to the full message
    full_msg += msg.decode("utf-8")

print(full_msg)
