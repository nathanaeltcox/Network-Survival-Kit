#/usr/bin/env python
"""This module is to scan for open ports."""
import socket
import time
import sys

def port_scan(ip_addr, rng, timer, output):
    if timer == True:
        start = time.time()
    rng_splt = rng.split("-")
    rng_one = int(rng_splt[0])
    rng_two = int(rng_splt[1])
    open_ports = []
    try:
        for port in range(rng_one,rng_two):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip_addr[0], port))
            if result == 0:
                print("Port {}:  Open".format(port))
                open_ports.append(port)
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
    if timer == True:
        seconds = time.time() - start
        print("Total time to scan took: {} sec.".format(seconds))
    if output != None:
        test = output[0]
        diff = len(test) - 5
        ctr = 0
        while ctr <= diff: #Tests whether user input ".txt" as part of their file name. Adds automatically if not.
            test = test[:0] + test[(1):]
            ctr += 1
        if test == ".txt":
            output_file = open(output[0], "a")
        else:
            output_file = open("{}.txt".format(output[0]), "a")
        output_file.write("Open Ports for Target {}:".format(ip_addr[0]) +
                            "\n""================================""\n")
        for x in open_ports:
            output_file.write("\n""Port {}: Open".format(x))
        if timer == True:
            output_file.write("\n""\n""Total time to scan took: {} sec.".format(seconds))
        output_file.write("\n""\n")