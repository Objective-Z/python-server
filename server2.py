import socket

host = ''
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
while True:
	c, addr = s.accept()
	print ("got connection from", addr)
	c.send(b"thanks for connecting")
	#c.close()
	while addr != None:
		print (c.recv(1024))
		message = raw_input(">")
		c.send(str.encode(message))
	c.close()