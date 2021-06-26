import os.path
import sys
from time import sleep

ip_list = [];
ip_file = None; #write ip file full path for auto load

def get_ips():
	global ip_list;
	return ip_list;

def set_ips(new_ip_list):
	global ip_list;
	ip_list = new_ip_list;

def ip_file_valid():
	global ip_list, ip_file;

	if(ip_file == None):
		ip_file = input("# enter full path for IP's file: ");

	if(ip_file == ""):
		ip_file = None
		ip_file_valid()
	elif(os.path.isfile(ip_file)):
		name = return_file_name(ip_file);
		print("# file '{}' is loaded -/".format(name));
		print("# extracting ip addresses! ");
		sleep(2);
		selected_file = open(ip_file, 'r');

		#move cursor to the start of the file
		selected_file.seek(0);
		#read file lines and convert it to a list
		ip_list = selected_file.readlines();

		#clearing '\n' from the strings of the list
		for index, ip in enumerate(ip_list):
			if("\n" in ip):
				ip_list[index] = ip[0:-1];

		selected_file.close();

	else:
		print("$ file '{}' doesn't exist or file path is incorrect!".format(ip_file));
		command = input("# enter 'q' to exit or press Enter to Retry! ");
		if(command == 'q' or command == 'Q'):
			sys.exit()
		else:
			ip_file_valid()


def return_file_name(path):
	file_name = ""
	name = ""
	index = -1

	while True:
		name = path[index]
		if name == '\\' or name == '/':
			break;
		else:
			file_name += name;
			index -= 1;


	return file_name[::-1];