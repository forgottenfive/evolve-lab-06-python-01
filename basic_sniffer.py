import socket, sys

try: 
	raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
		
except socket.error as e:
	print ("Error occured while creating socket. Error code: " + str(e[0]) + ", Error message " + e[1])
	sys.exit()

while True:
	packet=raw_socket.recvfrom(2048)
	print (packet)

