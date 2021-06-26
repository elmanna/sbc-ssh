import sys
from ip_file_valid import ip_file_valid as load_ips;
from ip_file_valid import get_ips, set_ips;
from ip_addr_valid import ip_addr_valid as validate_ips;
from ip_check_reachability import ip_check_reachability as ips_test; #returns list of  the  reachable ips
from ssh_connection import load_files, get_credentials, ssh_connection; #loading the credentials & commands files.
from create_threads import create_threads;

def main():
	print("{#}--->>> if u are dropping the file to the terminal/cmd be sure to remove whitespaces at the end of the path");
	load_ips(); #load ips file
	ips_list = get_ips(); #get the ips from the file
	print(ips_list);
	validate_ips(ips_list);
	set_ips(ips_test(ips_list)); #set the reachable ips list
	reachable_ips = get_ips(); #get the reachable ips list again
	print("{#}--->>> Reachable IPs %s"%(reachable_ips))
	load_files();
	credentials = get_credentials();
	create_threads(reachable_ips, credentials, ssh_connection);


if __name__ == '__main__':
	main()
