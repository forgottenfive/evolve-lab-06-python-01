import socket, sys

try: 
	raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_RAW)
	print (type(socket))
except socket.error as e:
	print ("Error occured while creating socket. Error code: " + str(e[0]) + ", Error message " + e[1])
	sys.exit()

