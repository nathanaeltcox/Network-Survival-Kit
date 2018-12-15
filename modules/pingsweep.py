#!/usr/bin/env python
import subprocess
import time
import sys

def ping_sweep(ip_addr, requests, timer, outpt):
    if timer == True:
        start = time.time()
    dots = 0
    for char in ip_addr[0]: #For loop makes it so that it works whether user inputs IP as "x.x.x." or forgets the last period and puts "x.x.x"
        if char == ".":
            dots += 1
        if dots == 3:
            ip_target = ip_addr[0]
        else:
            ip_target = ip_addr[0] + "."
    lat_req = requests[0]
    ip_result = [] #Stores the active IP addresses that are returned.
    ip_response = [] #Stores the time for each ping.
    ip_list = [] #Stores the active IP addresses as a list to be printed.
    for ip in range(0,256):
        output = b""
        ip_call = ip_target + str(ip)
        argument = "fping -a -C {} -q  {}".format(lat_req, ip_call)
        try:
            output = subprocess.check_output(argument, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as error:
            e = error.output  #Thanks to Matt Gluck for figuring out this part of the code.
        except KeyboardInterrupt:
            print("\n""User interrupted scan.")
            sys.exit()
        output = output.decode("utf-8")
        output = output.split(" ",2)
        ip_result = output[0]
        if ip_result == "":
            ip_response = ""
        else:
            ip_response = output[2]
            print("{} is detected online. Response time(s) were: {}".format(ip_result, ip_response))
            ip_list.append(ip_result)
    print("The following hosts were found to be online and responding to ping requests:")
    print("\n""Detected Hosts:")
    print("==============")
    print("\n".join(ip_list))
    if timer == True:
        seconds = time.time() - start
        print("\n""Total time to scan took: {} sec".format(seconds))
    if outpt != None:
        test = outpt[0]
        diff = len(test) - 5
        ctr = 0
        while ctr <= diff: #Tests whether user input ".txt" as part of their file name. Adds automatically if not.
            test = test[:0] + test[(1):]
            ctr += 1
        if test == ".txt":
            output_file = open(outpt[0], "w")
        else:
            output_file = open("{}.txt".format(outpt[0]), "w")
        output_file.write("The following hosts were found to be online and responding to ping requests:""\n"
                            "\n""Detected Hosts:"
                            "\n""===============")
        for line in ip_list:
            output_file.write("\n" + line)
        if timer == True:
            output_file.write("\n""\n""Total time to scan took: {} sec.".format(seconds))