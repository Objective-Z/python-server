# python-server
playing around with python's network features using TCP sockets. 

The current files in this repo are server2.py and client2.py.  

#server2.py
This file starts a server by opening a TCP socket and listening for incoming connections.  It then allows the client to send messages to the server ans for the server to send messages to the client.  

#client2.py
Connects to server through an open TCP socket. Once connected, the client can send data to the server (including files). 