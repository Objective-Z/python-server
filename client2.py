import socket

HOST = "130.203.69.20"
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

while True:
	print (s.recv(1024))
	message = raw_input(">")
	s.send(str.encode(message))
#s.close()