#!/usr/bin/env python3 

# Script Name:                  ops401d8-day11
# Author:                       Jonathan McMullin
# Date of latest revision:      07/24/2023
# Purpose:                      TCP Port Range Scanner

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Warning: only use on targets with appropriate permission

# Import libraries


import ipaddress
from scapy.all import ICMP, IP, sr1

def ping_sweep():
    global ip_list
    global host_count

    # Send ICMP request to each host on list
    for host in ip_list:
        # Skip network address and broadcast address
        if host in (ip_list.network_address, ip_list.broadcast_address):
            continue
            
        response = sr1(IP(dst=str(host)) / ICMP(), timeout=1, verbose=0)

        if response is None:
            print(f"Host {host} is down or unresponsive.")
        elif int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
            print(f"Host {host} is actively blocking ICMP traffic.")
        else:
            print(f"Host {host} is responding.")
            host_count += 1 

def main():
    global ip_list
    global host_count

    # Prompt user for network address in CIDR notation
    network = input("Enter network address in CIDR notation (e.g., x.x.x.x/24): ")
    ip_list = ipaddress.IPv4Network(network).hosts()
    host_count = 0

    # Display menu and perform actions based on user choice
    while True:
        print("ICMP Ping Sweep Tool Menu:")
        print("1. Perform ICMP Ping Sweep")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ping_sweep()
            print(f"Total hosts online: {host_count}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()