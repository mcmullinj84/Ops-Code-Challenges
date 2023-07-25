#!/usr/bin/env python3 

# Script Name:                  ops401d8-day11
# Author:                       Jonathan McMullin
# Date of latest revision:      07/24/2023
# Purpose:                      TCP Port Range Scanner

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Warning: only use on targets with appropriate permission

import sys
import scapy.all as scapy
from scapy.all import sr1, IP, TCP, send

def scan_port(host, port):
    src_port = 22  # Replace with your desired source port
    response = sr1(IP(dst=host) / TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)

    if response is None:
        print(f"Port {port} is filtered (silently dropped).")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            send(IP(dst=host) / TCP(sport=src_port, dport=port, flags="R"), verbose=0)
            print(f"Port {port} is open.")
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {port} is closed.")
    else:
        print(f"Port {port} is in an unknown state.")

def main():
    host = "scanme.nmap.org"  # Replace w/ target hostname or IP address
    port_range = range(20, 81)  # Replace w/ desired port range

    # Sends a single ping and prints out the response packet
    p = sr1(IP(dst=host) / scapy.ICMP(), verbose=0)
    if p:
        p.show()

    for port in port_range:
        scan_port(host, port)

if __name__ == "__main__":
    main()