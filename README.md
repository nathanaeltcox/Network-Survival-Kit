# Network-Survival-Kit
Multipurpose tool for network reconnaissance.

Conduct a pingsweep to find alive hosts on a network, scan for open ports on a given host, or look up manufacturer data for a given mac address.
When everythin is completed, collect it all in a single report.

To install: This script is designed to be run on a Kali Linux machine in a Python 3 environment. Place a copy in the directory where you keep your
scripts. Place the modules in a sub-directory called "modules" in the same directory as your nsk.py file.

To run: Run in the command line using "python nsk.py [argument]", with [argument] being replaced with one of the following:
	1. "pingsweep" to conduct a sweep for alive hosts,
	2. "portscan" to conduct a portscan of a given host,
	3. "maclookup" to look up the manufacturer data for a mac address, or
	4. "collect" to consolidate all your data in one file once you are finished.

Depending on which command you invoke, additional arguments will be required.

Ping sweep: when conducting a ping sweep, you will need to input the first three octets of the IP address for the network you wish to scan, like
this: "xxx.xxx.xxx." or "xxx.xxx.xxx". This function will track the latency times of the pings it sends out. If you want to specify how many
pings per IP, use the command "-c" followed by the number of pings. If you omit this command, it will default to 5. If you want to change the 
name of the output file, use "-o" or "--output". The default filename is "PingsweepResults.txt".

For example:
	python nsk.py pingsweep 10.0.0. (Pings all 256 IP addresses in the 10.0.0.0-255 range. Pings each 5 times and saves output to a file.
	python nsk.py pingsweep -c 4 10.0.0. (Uses four pings instead of five.)
	python nsk.py pingsweep -o PingsweepOutput 10.0.0 (Saves results to file "PingsweepOutput.txt" instead of "PingsweepResults.txt"

Port scan: When conducting a port scan, you will need to put in the target IP address. The scan will automatically scan all ports. If you want
to narrow down you scan, you can use the "-r" or "--range" argument, followed by the range of ports you want to scan (ex. 10-5000). If you want
to change the name of the file results are written to, use the "-o" or "--output" argument (see ping sweep section for example). The default
filename is "PortscanResults.txt".

For example:
	python nsk.py portscan 10.0.0.1 (Scans all ports on the IP address 10.0.0.1 and returns a list of open ports.)
	python nsk.py portscan -r 1-10000 10.0.0.1 (Scans only ports 1-10000 on IP 10.0.0.1 returns a list of open ports.)

Mac address lookup: When conducting a mac address lookup, you will need to input the mac address (or just the first half of the mac address).
Use the "-o" or "--output" argument to change the name of the file the results are written to. The default filename is "MacLookupResults.txt".

For example:
	python nsk.py maclookup 08:00:22 (Looks up the name and address of the manufacturer for devices bearing the mac address prefix 08:00:22).

Data collect: When collecting the data into one file, you need to input the names of all the files you wrote your results to, using the 
following arguments: "-ps" or "--pingsweep" for ping sweep, "-pscan" or "--portscan" for port scan, and "-maclu" or "--maclookup" for mac
address lookup. If you used the default filenames, no additional arguments needed. Use the argument "-o" or "--output" to choose the name of 
the file your results will be saved in. The default filename is "Report.txt".

For example:
	python nsk.py collect (Consolidates results from all previous scans in a single file called "Report.txt", assuming everything was 
saved using default filenames.)
	python nsk.py collect -ps PingsweepOutput (Consolidates results when the pingsweep results were saved as "PinsgweepOutput.txt" instead
of the default.)
