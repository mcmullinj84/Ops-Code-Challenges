#!/usr/bin/env python3

# Script Name:                  ops401d8-day36
# Author:                       Jonathan McMullin
# Date of latest revision:      08/28/2023
# Purpose:                      Web Application Fingerprinting

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

import subprocess
import socket

def banner_grab_netcat(target, port):
    try:
        # Create a socket and connect to the target
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Set a timeout for the connection attempt
            s.connect((target, port))
            banner = s.recv(1024).decode()
        print("Netcat Banner Grabbing:")
        print(banner)
    except (socket.error, TimeoutError) as e:
        print(f"Error: {e}")

def banner_grab_telnet(target, port):
    try:
        # Create a socket and connect to the target
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Set a timeout for the connection attempt
            s.connect((target, port))
            banner = s.recv(1024).decode()
        print("\nTelnet Banner Grabbing:")
        print(banner)
    except (socket.error, TimeoutError) as e:
        print(f"Error: {e}")

def banner_grab_nmap(target):
    try:
        # Run Nmap to scan the most popular ports (1-1000)
        command = f'nmap -p 1-1000 -sV -Pn {target}'
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print("\nNmap Banner Grabbing:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

def main():
    # Prompt the user for target address and port number
    target = input("Enter the URL or IP address: ")
    port = int(input("Enter the port number: "))  # Convert port to an integer

    # Perform banner grabbing using netcat
    banner_grab_netcat(target, port)

    # Perform banner grabbing using telnet
    banner_grab_telnet(target, port)

    # Perform banner grabbing using Nmap
    banner_grab_nmap(target)

if __name__ == "__main__":
    main()