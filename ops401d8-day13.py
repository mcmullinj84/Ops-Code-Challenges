#!/usr/bin/env python3 

# Script Name:                  ops401d8-day13
# Author:                       Jonathan McMullin
# Date of latest revision:      07/26/2023
# Purpose:                      IP Ping and Port Scan Tool

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Warning: only use on targets with appropriate permission

# import libraries

from scapy.all import ICMP, IP, sr1, TCP, send

# Functions 

# Function to scan ports
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

# Function to ask for user inputted IP, ping and if open call port scanning function
def ping_and_scan():
    target_ip = input("Enter the target IP address: ")

    # Perform ICMP ping sweep
    response = sr1(IP(dst=target_ip) / ICMP(), timeout=1, verbose=0)

    if response is None:
        print(f"Host {target_ip} is down or unresponsive.")
    elif int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
        print(f"Host {target_ip} is actively blocking ICMP traffic.")
    else:
        print(f"Host {target_ip} is responding.")
        # Call port scan function
        port_scan(target_ip)

# Function to prompt user for port range and call port scan function
def port_scan(host):
    port_range_str = input("Enter the port range (e.g., 20-80): ")
    start_port, end_port = map(int, port_range_str.split("-"))
    port_range = range(start_port, end_port + 1)

    for port in port_range:
        scan_port(host, port)

# Main 

if __name__ == "__main__":
    ping_and_scan()

# End