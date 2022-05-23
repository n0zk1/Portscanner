import sys
import socket
from datetime import datetime

target = input("Enter IP or a Host to scan: ")

tcp = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5900, 8080]
udp = [53, 67, 68, 69, 123, 135, 137, 138, 139, 161, 162, 445, 500, 514, 520, 631, 1434, 1900, 4500, 49152]

if len(target) > 2:
    targetIP = socket.gethostbyname(target)
else:
    print("\nPlease give a IP or a Host\nExiting script...")
    sys.exit()

print('\n')
print("*" * 55)
print("Scanning IP: " + target)
print("Scanning started at: " + str(datetime.now()))
print("*" * 55)
print('\n')
print("Select a option")

input = input(
    """
    1) Normal scan only 999 ports \n
    2) Scan all 65535 ports\n
    3) Scan Typical TCP ports\n
    4) Scan Typical UDP ports\n 
    5) Scan Both TCP and UDP ports\n
    """)

print("\n")

if input == '1':

    print("Staring a normal scan of 999 ports\n")

    try:
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                print("Port {} is open".format(port))

            s.close()

    except KeyboardInterrupt:
        print("\n Exiting the script ")
        sys.exit()
    except socket.gaierror:
        print("\n Could not find IP or Host ")
        sys.exit()
    except socket.error:
        print("\n Server do not respond ")
        sys.exit()

elif input == '2':
    print("Staring scan of all 65535 ports\n")

    try:
        for port in range(1, 1000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                print("Port {} is open".format(port))

            s.close()

    except KeyboardInterrupt:
        print("\n Exiting the script ")
        sys.exit()
    except socket.gaierror:
        print("\n Could not find IP or Host ")
        sys.exit()
    except socket.error:
        print("\n Server do not respond ")
        sys.exit()

elif input == '3':
    print("Starting a TCP port scan\n")

    try:
        for port in tcp:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                print("Port {} is open".format(port))

            s.close()

    except KeyboardInterrupt:
        print("\n Exiting the script ")
        sys.exit()
    except socket.gaierror:
        print("\n Could not find IP or Host ")
        sys.exit()
    except socket.error:
        print("\n Server do not respond ")
        sys.exit()

elif input == '4':
    print("Starting a UDP port scan\n")

    try:
        for port in udp:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                print("Port {} is open".format(port))

            s.close()

    except KeyboardInterrupt:
        print("\n Exiting the script ")
        sys.exit()
    except socket.gaierror:
        print("\n Could not find IP or Host ")
        sys.exit()
    except socket.error:
        print("\n Server do not respond ")
        sys.exit()

elif input == '5':
    print("Starting both a TCP and UDP port scan\n")

    try:
        for port in tcp + udp:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                print("Port {} is open".format(port))

            s.close()

    except KeyboardInterrupt:
        print("\n Exiting the script ")
        sys.exit()
    except socket.gaierror:
        print("\n Could not find IP or Host ")
        sys.exit()
    except socket.error:
        print("\n Server do not respond ")
        sys.exit()
