import sys, time, os.path, re, paramiko;
from ip_file_valid import return_file_name

#Globals
credens_dict = {};
credentials_file = None #write credentials file full path for auto load
commands_file = None #write commands file full path for auto load


def load_files():
	global credentials_file, commands_file
	#Username/Password -> File
	if(credentials_file == None):
		credentials_file = input("# Enter the path for the credentials file: ");

	#check for existence
	if os.path.isfile(credentials_file):
		name = return_file_name(credentials_file);
		print("-> credentials file '{name}' is loaded".format(name=name));
	else:
		print("-> file doesn't exist! or path is incorrect, retry...");
		credentials_file = None
		load_files();

	#Commands -> File
	if(commands_file == None):
		commands_file = input("# Enter the path for the commands file: ");
		#check for existence
		if os.path.isfile(commands_file):
			name = return_file_name(commands_file);
			print("-> commands file '{name}' is loaded".format(name=name));
		else:
			print("-> file doesn't exist! or path is incorrect, retry...");
			commands_file = None;
			load_files();


def get_credentials():
	global credentials_file, credens_dict;

	credens = open(credentials_file, 'r');
	credens.seek(0);
	_list_ = credens.readlines();
	credens.close()
	
	for index, line in enumerate(_list_):
		line = line.rstrip("\n");
		_temp_list_ = line.split(',');
		credens_dict[index] = _temp_list_;

	return credens_dict;



def ssh_connection(ip, username, password):
	global commands_file;

	try:
		try:
			session = paramiko.SSHClient();
			session.set_missing_host_key_policy(paramiko.AutoAddPolicy());
		except Exception as e:
			print("{!@}--->>> Error in establishing the connection using SSH");
			sys.exit();
		
		try:
			session.connect(hostname=ip, username=username, password=password); 
		except Exception as e:
			print("error in connecting into the switch");
			print("ip: {ip} username: {user} password: {passw}".format(ip=ip, user=username, passw=password));
		#nodename nor servname provided, or not known
		conn = session.invoke_shell();

		#enable full length for output return from the shell
		conn.send("enable \n");
		conn.send("terminal length 0 \n");
		time.sleep(2);

		#enter configure mode in the arista switch
		conn.send("\n");
		conn.send("configure terminal \n");
		time.sleep(2);

		#load commands from commads files & send them
		commands = open(commands_file, 'r');
		commands.seek(0);

		for each in commands.readlines():
			conn.send("{command} \n".format(command=each));
			time.sleep(2);

		commands.close();

		#reciving the output of the commands
		switch_output = conn.recv(65535); 

		if re.search(b"% Invalid input ", switch_output):
			print("[!@]--->>> % Invalid input detected form {ip} .".format(ip=ip));
		else:
			print("[#]--->>> all commands were sent & executed successfully to {ip} .".format(ip=ip));

		print("\n\n\n-----------------[OUTPUT]-----{IP}-[%s]------"%(ip));
		print(switch_output.decode("ascii") + "\n\n\n");
		session.close();

		return 0;

	except paramiko.AuthenticationException:
		print("[!@]--->>> Invalid username or password in {ip} .".format(ip=ip));

		return -1;
