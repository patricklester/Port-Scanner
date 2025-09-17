#Port Scanner
#Connects to different ports on the target machine and checks which ports are open
#Only used to scan my own machine

import socket
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
sock.settimeout(1) 
result = sock.connect_ex(("127.0.0.1", 80)) #Local host, checking port 80
sock.close()

#--------------------- Code 1 ----------------------

##Print:

if result == 0:
    print("Port 80 is open")
else:
    print("Port 80 is closed")
                                        """


def port_check(host, port):
    """Function to check openness on a port"""
    
    #AF_INET signals to use IPv4 addresses
    #SOCK_STREAM signals to use TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)#Gives up after one second
    result = sock.connect_ex((host, port)) #connect_ex is what is trying to connect to host and port
    sock.close #closes the socket

    return result == 0
target = "127.0.0.1" #This is localhost, using other IP's is illegal
common_ports = [22, 80, 443, 3389, 53, 25] #SSH, HTTP, HTTPS, RDP, DNS, SMTP

for port in common_ports:
    if port_check(target, port): #call the function to get the port with the common ports
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED.")
