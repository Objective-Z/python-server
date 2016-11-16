import socket

HOST = "130.203.162.4" #host server
PORT = 12345 #port to reserve
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #opens a TCP socket connection

s.connect((HOST, PORT)) #connects to host through port with socket connection

while True:
	print (s.recv(1024)) #prints data recieved from the host
	message = raw_input(">") #message to be sent to server
	if message == 'send file': #if user types "send file"...
		path = raw_input() #path of file to send
		f = open(path) #open file
		l = f.read(1024) #read each line of the file and store it in  a variable
		while l:
			#l = f.read(1024) #read each line of the file and store it in  a variable
			s.send(l) #send a line of the file
			l = f.read(1024)
		f.close()
	else: #if user enters something that is not "send file"...
		s.send(str.encode(message)) #send the message to server as byte code
	