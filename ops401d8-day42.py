#!/usr/bin/env python3

# Script Name:                  ops401d8-day42
# Author:                       Jonathan McMullin
# Date of latest revision:      09/07/2023
# Purpose:                      Pentest Toolkit - NMAP

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Check if NMAP is installed on the host <pip install python-nmap> 

# Import Libraries

import nmap

# Functions 

# Main

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Full Scan\n""")
print("You have selected option: ", resp)

port_range = input("Enter the port range (e.g., 1-100): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", list(scanner[ip_addr]['tcp'].keys()))
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", list(scanner[ip_addr]['udp'].keys()))
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    open_ports = []
    for protocol in scanner[ip_addr].all_protocols():
        open_ports.extend(list(scanner[ip_addr][protocol].keys()))
    print("Open Ports: ", open_ports)
else:
    print("Please enter a valid option.")

# End
