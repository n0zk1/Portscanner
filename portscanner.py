import sys
import socket
from datetime import datetime

target = input("Enter host to scan: ")

if len(target) > 2:

        targetIP = socket.gethostbyname(target)
else:
        print("nothing")

print('\n')
print("*" * 10)
print("Scanning target: " + target)
print("Scanning target started at:" + str(datetime.now()))
print("*" * 10)

input = input("1 or 2")

if input == '1':
        try:
                for port in range(1,65535):
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(1)

                        result = s.connect_ex((target,port))

                        if result ==0:

                                print("Port {} is open".format(port))

                        s.close()


        except KeyboardInterrupt:
                print("\n Exiting script")
                sys.exit()
        except socket.gaierror:
                print("\n Could not find host")
                sys.exit()
        except socket.error:
                print("\ No response")
                sys.exit()
                                                               
