import socket, sys, binascii, struct

try: 
	raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))		
except socket.error as e:
	print ("Error occured while creating socket. Error code: " + str(e[0]) + ", Error message " + e[1])
	sys.exit()

while True:
	packet=raw_socket.recvfrom(2048)
	ethernet_header = packet[0][0:14]
	eth_hdr = struct.unpack("!6s6s2s", ethernet_header)
	type(eth_hdr)
#	print ("Destination: " + binascii.hexlify(eth_hdr[0]) + "Source:" + binascii.hexlify(eth_hdr[1]) + "Type: " + binascii.hexlify(eth_hdr[2]))
	print ("Destination: " , binascii.hexlify(eth_hdr[0]), "Source:" , binascii.hexlify(eth_hdr[1]), "Type: " , binascii.hexlify(eth_hdr[2]))
#	print ("Destination: " ,binascii.hexlify(eth_hdr[0]))
	ip_header = packet[0][14:34]
	ip_hdr = struct.unpack("!12s4s4s", ip_header)
#	print (type(ip_hdr[1]))
#	print (ip_hdr[1])
#	print (socket.inet_ntoa(ip_hdr[1]))
	print ("Source IP: " + socket.inet_ntoa(ip_hdr[1]) + " Destination IP: " + socket.inet_ntoa(ip_hdr[2]))
