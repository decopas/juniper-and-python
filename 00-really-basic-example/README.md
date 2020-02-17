How to execute this script

1)Verify the file "BasicShows" exists

###################
root@vMX01:/var/db/scripts/op # more BasicShows
show version
show system uptime


2)Verifiy Junos configuration
####################
root@vMX01> show configuration groups PYTHON |display set 
set groups PYTHON system scripts op file python0.py command pyshoot0
set groups PYTHON system scripts language python


3) Execute script

####################
root@vMX01> op pyshoot0  
>>>show version


>>>show system uptime
