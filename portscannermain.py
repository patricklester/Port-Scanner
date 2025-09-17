#Port Scanner
#Connects to different ports on the target machine and checks which ports are open
#Only used to scan my own machine

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
sock.settimeout(1) 
result = sock.connect_ex(("127.0.0.1", 80))
sock.close()

#--------------------- Code 1 ----------------------

##Print:

if result == 0:
    print("Port 80 is open")
else:
    print("Port 80 is closed")

    