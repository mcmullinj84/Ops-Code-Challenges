#!/usr/bin/env python3 

# Script Name:                  ops401d8-day12
# Author:                       Jonathan McMullin
# Date of latest revision:      07/24/2023
# Purpose:                      TCP Port Range Scanner

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Warning: only use on targets with appropriate permission

# Import libraries


import ipaddress
from scapy.all import ICMP, IP, sr1, TCP, send

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

def ping_sweep():
    global ip_list
    global host_count

def main():
    global ip_list
    global host_count

    while True:
        print("Tool Menu:")
        print("1. ICMP Ping Sweep")
        print("2. TCP Port Range Scanner")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # ICMP Ping Sweep mode
            network = input("Enter network address in CIDR notation (e.g., x.x.x.x/24): ")
            ip_list = ipaddress.IPv4Network(network).hosts()
            host_count = 0
            ping_sweep()
            print(f"Total hosts online: {host_count}")
        elif choice == "2":
            # TCP Port Range Scanner mode
            host = input("Enter the target hostname or IP address: ")
            port_range_str = input("Enter the port range (e.g., 20-80): ")
            start_port, end_port = map(int, port_range_str.split("-"))
            port_range = range(start_port, end_port + 1)
            for port in port_range:
                scan_port(host, port)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()