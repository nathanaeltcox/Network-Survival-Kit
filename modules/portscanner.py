#/usr/bin/env python
"""This module is to scan for open ports."""
import socket
import sys

def port_scan(ip_addr,rng):
    rng_splt = rng.split("-")
    rng_one = int(rng_splt[0])
    rng_two = int(rng_splt[1])
    try:
        for port in range(rng_one,rng_two):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip_addr[0], port))
            if result == 0:
                print("Port {}:  Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("User interrupted scan.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

"""def port_scan(ip_addr,rng):
    print("IP address is: " + ip_addr[0])
    print("The range is: " + rng)
    the_real_range = rng.split("-")
    range_one = the_real_range[0]
    range_two = the_real_range[1]
    print("The range goes from: " + range_one)
    print("to: " + range_two)"""