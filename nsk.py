#!/usr/bin/env python
import argparse

#Super wordy way to import.
#import modules.pingsweep
#import modules.traceroute

#Efficient alias way to import.
#import modules.pingsweep as ps
#import modules.traceroute as ts
#import modules.portscanner as pscan

#Import explicit functions.
from modules.pingsweep import pingsweep as ps, set_ttl
from modules.traceroute import traceroute as tr
from modules.portscanner import port_scan as pscan

def pingsweep(args):
    ps(args.ip)
    set_ttl(1200)
    ps(args.ip)

def traceroute(args):
    tr(args.target)

def portscanner(args):
    pscan(args.ip, args.range)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Network Survival Kit", 
                                    description="Command line network toolkit.")
    
#    parser.add_argument("ip", nargs=1, default="127.0.0.1", help="Taget IP address")
#    parser.add_argument("--port", "-p", type=int)
#    parser.add_argument("--protocol", "-P", nargs="?", default="tcp", 
#                        choices=["tcp", "udp", "icmp"])
    parser.add_argument("--output", "-o", nargs=1, help="File name to write results to")

    subparsers = parser.add_subparsers(help="Module specific utilities.")

    parser_pingsweep = subparsers.add_parser("pingsweep", help="Perform network ping sweep")
    parser_pingsweep.add_argument("ip", nargs=1, help="Target IP address")
    parser_pingsweep.set_defaults(func=pingsweep)
 
    parser_traceroute = subparsers.add_parser("traceroute", help="Track hops from host to target")
    parser_traceroute.add_argument("target", nargs=1, help="Target host to trace path to")
    parser_traceroute.set_defaults(func=traceroute)

    parser_portscanner = subparsers.add_parser("portscanner", help="Find open ports at IP address location")
    parser_portscanner.add_argument("ip", nargs=1, help="Target IP address")
    parser_portscanner.add_argument("--range", "-r", nargs="?", default="1-65536", help="Range of ports to scan")
    parser_portscanner.set_defaults(func=portscanner)

    args = parser.parse_args()
    args.func(args)
    print("Arguments: {}".format(args))