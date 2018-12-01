#/usr/bin/env python
"""This module collects and consolidates the data from scans in one file."""

def data_collect(output, ps, pscan, maclu):
    file_names = [ps[0], pscan[0], maclu[0]]
    test1 = output[0]
    diff = len(test1) - 5
    ctr = 0
    while ctr <= diff: #Tests whether user input ".txt" as part of their file name. Adds automatically if not.
        test1 = test1[:0] + test1[(1):]
        ctr += 1
    if test1 == ".txt":
        output_file = open(output[0], "w")
    else:
        output_file = open("{}.txt".format(output[0]), "w")
    output_file.write("Report of Network Reconaissance:""\n""\n")
    for x in range(0,3):
        test2 = file_names[x]
        diff = len(test2) - 5
        ctr = 0
        while ctr <= diff:
            test2 = test2[:0] + test2[(1):]
            ctr += 1
        if test2 == ".txt":
            input_file = open(file_names[x], "r")
        else:
            input_file = open("{}.txt".format(file_names[x]), "r")
        for line in input_file:
            output_file.write(line)
        output_file.write("\n""\n")
        