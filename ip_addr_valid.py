import sys


def ip_addr_valid(list):
	for index, ip in enumerate(list):
		#split ip into 4 indices for validation checkup
		_ip_ = ip;
		ip = ip.split(".")

		if ((len(ip) == 4) and (1 <= int(ip[0]) <= 223) and (int(ip[0]) != 127) and (int(ip[0]) != 169 or int(ip[1]) != 254) and (0 <= int(ip[1]) <= 255) and (0 <= int(ip[2]) <= 255) and (0 <= int(ip[3]) <= 255)):
			pass
		else:
			print("{!@}--->>> ip {ip}  is invalid".format(ip=_ip_));
			sys.exit()