#!/usr/bin/env python3

# Script Name:                  ops401d8-day36
# Author:                       Jonathan McMullin
# Date of latest revision:      08/28/2023
# Purpose:                      Web Application Fingerprinting
# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

import subprocess

def banner_grab_netcat(target, port):
    try:
        # Use subprocess to run netcat and capture its output
        command = f'nc -v {target} {port}'
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print("Netcat Banner Grabbing:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

def banner_grab_telnet(target, port):
    try:
        # Use subprocess to run telnet and capture its output
        command = f'telnet {target} {port}'
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print("\nTelnet Banner Grabbing:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

def banner_grab_nmap(target):
    try:
        # Use subprocess to run Nmap and capture its output
        command = f'nmap -p 1-65535 -sV -Pn {target}'
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print("\nNmap Banner Grabbing:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

def main():
    # Prompt the user for target address and port number
    target = input("Enter the URL or IP address: ")
    port = input("Enter the port number: ")

    # Perform banner grabbing using netcat
    banner_grab_netcat(target, port)

    # Perform banner grabbing using telnet
    banner_grab_telnet(target, port)

    # Perform banner grabbing using Nmap
    banner_grab_nmap(target)

if __name__ == "__main__":
    main()
