#wol.py

import sys
import socket


def macHandler(MAC_address):
	mac_to_array = MAC_address.split()
	packet_pre_data = 0
	for byte in mac_to_array:
		packet_pre_data = packet_pre_data + chr(hex(byte))
		return packet_pre_data

def magicPacketGen(packet_pre_data):
	for index in range(6):
		magic_packet = hex(255)
	
	for index in range(16):
		magic_packet = magic_packet + packet_pre_data

	return magic_packet


def socketHandler(socket, broadcast_address, magic_packet):
	dest = {broadcast_address, 80}
	socket.sendto(bytes(512), dest)
	socket.close()
	all_vars = {
		"socket" : socket,
		"magic_packet" : magic_packet,
		"len(magic_packet)"	: len(magic_packet),
		"broadcast_address" : broadcast_address,
		"dest"	: dest
	}
	return all_vars;
					

usage = "Usage: python wol.py <'mac_address'> <'broadcast_address'>"
if len(sys.argv) < 2:
	print(usage)
else:	
	mac_address = sys.argv[0]
	broadcast_address = sys.argv[1]
	package_pre_data = macHandler(broadcast_address)
	magic_packet = magicPacketGen(package_pre_data)
	socket = socket.socket()
	handler_callback = socketHandler(socket, broadcast_address, magic_packet)
	print(handler_callback)
