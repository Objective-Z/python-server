import socket

HOST = "130.203.69.20"
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

while True:
	print (s.recv(1024))
	message = raw_input(">")
	if message == 'send file':
		path = raw_input()
		f = open(path)
		l = f.read(1024)
		s.send(b"someone is sending you a file...\n" + l)
		#s.send(l)
	else:
		s.send(str.encode(message))
	
#s.close()