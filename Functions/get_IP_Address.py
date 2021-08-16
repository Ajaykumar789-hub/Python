#getting ip address using python

import socket

hostname=socket.gethostname()

ipaddr=socket.gethostbyname(hostname)
#ip2=socket.gethostname(hostname)

print(ipaddr) #printing ip address 
print(hostname) 