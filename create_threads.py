import threading;


def create_threads(ips, credens_dict, func):
	threads = [];


	for index, ip in enumerate(ips):
		thread = threading.Thread(target=func, args=(ip, credens_dict[index][0], credens_dict[index][1], ));
		thread.start();
		threads.append(thread);

	for thread in threads:
		thread.join();