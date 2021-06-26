import sys, subprocess;
from subprocess import DEVNULL;

def ip_check_reachability(list):
	reachable = []
	for ip in list:
		#send 2 ping  requests to check if is reachable, if its it returns 0.  stdout is disabled & aslo the stderr  
		if(sys.platform == 'darwin'):
			ping_replay = subprocess.call("ping %s -c 2 " %(ip),stdout=DEVNULL, stderr=DEVNULL, shell=True);
		elif(sys.platform == 'win32'):
			ping_replay = subprocess.call("ping %s -n 2 " %(ip),stdout=DEVNULL, stderr=DEVNULL);
		elif(sys.platform == 'linux' or sys.platform == 'linux2'):
			ping_replay = subprocess.call("ping %s -c 2 " %(ip),stdout=DEVNULL, stderr=DEVNULL);
			
		if ping_replay == 0:
			print("-> IP {ip} is reachable. \n".format(ip=ip));
			reachable.append(ip);
			continue
		else:
			print("-> IP {ip} is **unreachable**. \n".format(ip=ip));
			command = input("{!}--->>> exit? ('y' to abort or 'n' to proceed): ");
			if(command == 'y' or command ==  'Y'):
				sys.exit();
			else:
				continue

	if(len(reachable) == 0):
		print("{!@}--->>> there is no reachable ip from the loaded file, exiting...");
		sys.exit();

	return reachable;