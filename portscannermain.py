#Port Scanner
#Connects to different ports on the target machine and checks which ports are open
#Only used to scan my own machine

import socket
import threading


def thread_scanner(host, start, end):
    threads = [] #list for all of the threads
    for port in range(start, end):
        t = threading.Thread(target=port_check, args=(host, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def port_check(host, port):
    """Function to check openness on a port"""
    
    #AF_INET signals to use IPv4 addresses
    #SOCK_STREAM signals to use TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.5)#Gives up after one second
    result = sock.connect_ex((host, port)) #connect_ex is what is trying to connect to host and port
    sock.close() #closes the socket

    return result == 0
def main():
    target = input("Enter IP: ")
    start = int(input("Enter starting port #: "))
    end = int(input("Enter ending port #: "))

    for port in range(start, end + 1):
        if port_check(target, port):
            print(f"Port: {port}, OPEN")
        else:
            print(f"Port: {port}, CLOSED")

    thread_scanner(target, start, end)

if __name__ == "__main__":
    main()