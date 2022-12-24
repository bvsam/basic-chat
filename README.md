# Basic Chat

This program allows clients to connect to a server and chat with each other over the terminal.

It also acts as a demo to test out creating a basic TCP/IP server and client in Python using sockets.

This project was based off the [sockets tutorial](https://www.youtube.com/watch?v=Lbfe3-v7yE0&list=PLQVvvaa0QuDdzLB_0JSTTcl8E8jsJLhR5) from Sentdex.

## Usage

An installation of Python is a prerequisite to run the program. Run the following commands:

```
git clone https://github.com/bvsam/basic-chat.git
cd basic-chat
py server.py
```

In a new terminal, run the following commands to start the client interface:

```
cd basic-chat
py client.py
```

Multiple clients can be running and connected to the server simultaneously. Once a username has been entered, hit Enter at any time to receive the latest messages that have been sent by other clients. Type a message and hit Enter to send a message to other clients.
