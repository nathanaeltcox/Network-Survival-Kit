#/usr/bin/env python
"""This module looks up the manufacturer of a given mac address."""
import json
import urllib.request
import time

def mac_lookup(mac, timer, outpt):
    if timer == True:
        start = time.time()
    url = "http://macvendors.co/api/{}".format(mac[0])
    req = urllib.request.Request(url)

    r = urllib.request.urlopen(req).read()
    counter1 = 3
    counter2 = 5
    mac_info = {}

    output = r.decode("utf-8")
    output = output.split('"')
    while counter2 <= 29:
        mac_info.update({output[counter1] : output[counter2]})
        counter1 += 2
        counter2 += 2

    print("Company name and address: {}, {}".format(mac_info["company"], mac_info["address"]))
    if timer == True:
        seconds = time.time() - start
        print("Time to retrieve: {} sec.".format(seconds))
    if outpt != None:
        test = outpt[0]
        diff = len(test) - 5
        ctr = 0
        while ctr <= diff: #Tests whether user input ".txt" as part of their file name. Adds automatically if not.
            test = test[:0] + test[(1):]
            ctr += 1
        if test == ".txt":
            output_file = open(outpt[0], "a")
        else:
            output_file = open("{}.txt".format(outpt[0]), "a")
        output_file.write("Company name and address for host {}:".format(mac[0]) + "\n" + "{}, {}".format(mac_info["company"], mac_info["address"]))
        if timer == True:
            output_file.write("\n""\n""Time to retrieve: {} sec.".format(seconds))
        output_file.write("\n""\n")