#!/usr/bin/env python
import argparse

#Import explicit functions.
from modules.pingsweep import ping_sweep as ps
from modules.portscan import port_scan as pscan
from modules.macaddresslookup import mac_lookup as maclu
from modules.datacollect import data_collect as dcol

def pingsweep(args):
    ps(args.ip, args.c, args.time, args.output)

def portscan(args):
    pscan(args.ip, args.range, args.time, args.output)

def macaddresslookup(args):
    maclu(args.mac, args.time, args.output)

def datacollect(args):
    dcol(args.output, args.pingsweep, args.portscan, args.maclookup)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Network Survival Kit", 
                                    description="Command line network toolkit.")
    
    parser.add_argument("--time", "-t", help="Time the function", action="store_true")

    subparsers = parser.add_subparsers(help="Module specific utilities.")

    parser_pingsweep = subparsers.add_parser("pingsweep", help="Perform network ping sweep")
    parser_pingsweep.add_argument("ip", nargs=1, help="Target IP address")
    parser_pingsweep.add_argument("-c", nargs="?", default="5", help="Number of requests to send to host; tracks latency times")
    parser_pingsweep.add_argument("--output", "-o", nargs=1, default=["PingsweepResults"], help="File name to write results to")
    parser_pingsweep.set_defaults(func=pingsweep)
 
    parser_portscan = subparsers.add_parser("portscan", help="Find open ports at IP address location")
    parser_portscan.add_argument("ip", nargs=1, help="Target IP address")
    parser_portscan.add_argument("--range", "-r", nargs="?", default="1-65536", help="Range of ports to scan")
    parser_portscan.add_argument("--output", "-o", nargs=1, default=["PortscanResults"], help="File name to write results to")
    parser_portscan.set_defaults(func=portscan)

    parser_macaddresslookup = subparsers.add_parser("maclookup", help="Get info on mac addresses")
    parser_macaddresslookup.add_argument("mac", nargs=1, help="Mac address to get info on")
    parser_macaddresslookup.add_argument("--output", "-o", nargs=1, default=["MacLookupResults"], help="File name to write results to")
    parser_macaddresslookup.set_defaults(func=macaddresslookup)

    parser_datacollect = subparsers.add_parser("collect", help="Collects and consolidates all data from other scans") 
    parser_datacollect.add_argument("--output", "-o", nargs=1, default=["Report"], help="File name to write results to")
    parser_datacollect.add_argument("--pingsweep", "-ps", nargs=1, default=["PingsweepResults"], help="Name of file to cellect data from")
    parser_datacollect.add_argument("--portscan", "-pscan", nargs=1, default=["PortscanResults"], help="Name of file to cellect data from")
    parser_datacollect.add_argument("--maclookup", "-maclu", nargs=1, default=["MacLookupResults"], help="Name of file to cellect data from")
    parser_datacollect.set_defaults(func=datacollect)

    args = parser.parse_args()
    args.func(args)
    print("Arguments: {}".format(args))