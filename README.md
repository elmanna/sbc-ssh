#################
-> 3 files are required for the process


1. ips txt file: should contain all of the ip's of the ssh hosting servers
that the commands in the commands file will be executed on,
each ip address should be placed in single line by its own

->> example src/ip.txt

2. commands txt file: should contains the commands 
that will be sent to the os hosting the ssh server

->> example src/commands.txt

3. credentials txt file: contains the ssh server hosting machine usernames & passwords
seprated by a comma ',' each credentials should be in a single line

->> example src/credentials.txt



#>>>>> 
files doesn't need to be only in the src folder
clould be any where in the file system just a full path should be applied (of-course)
 <<<<<<#