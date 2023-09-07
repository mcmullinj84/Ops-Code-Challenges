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

def menu():
    print("Simple Nmap Scanner")
    print("1. Quick Scan")
    print("2. Intense Scan")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def nmap_scan(target, scan_type):
    nm = nmap.PortScanner()
    if scan_type == "1":
        nm.scan(target, arguments="-T4 -F")
    elif scan_type == "2":
        nm.scan(target, arguments="-T4 -A")
    else:
        print("Exiting the program.")
        return

    print(f"Scanning target: {target}")
    print(f"Scan type: {scan_type}")
    print("Results:")
    for host, result in nm.all_hosts().items():
        print(f"Host: {host}")
        for proto, ports in result['tcp'].items():
            for port, port_info in ports.items():
                print(f"Port: {port} - State: {port_info['state']}")

# Main

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1" or choice == "2":
            target = input("Enter the target IP or domain: ")
            nmap_scan(target, choice)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# End
