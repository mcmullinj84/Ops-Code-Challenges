#!/usr/bin/env python3

# Script Name:                  ops401d8-day26
# Author:                       Jonathan McMullin
# Date of latest revision:      08/14/2023
# Purpose:                      Add logs to IP Ping and Port Scan Tool

# This script is based off of my original IP Ping/Port Scan tool
# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Warning: only use on targets with appropriate permission

# import libraries
import logging
import os
from scapy.all import ICMP, IP, sr1, TCP, send

# Configure logging to show all types of logs
log_level = os.environ.get("LOGLEVEL", "INFO")
logging.basicConfig(level=log_level)

# Function to send log output to a file
def setup_logging_file():
    # Establishes log file in local directory
    log_filename = "scanning_logs.txt"
    file_handler = logging.FileHandler(log_filename)
    # Creates time, level, and message log
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logging.getLogger().addHandler(file_handler)

# Function to scan ports - added logging at the debug and info levels
def scan_port(host, port):
    src_port = 22
    logging.debug(f"Scanning port {port} on host {host}.")
    response = sr1(IP(dst=host) / TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)

    if response is None:
        logging.debug(f"Port {port} is filtered (silently dropped).")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            send(IP(dst=host) / TCP(sport=src_port, dport=port, flags="R"), verbose=0)
            logging.info(f"Port {port} is open.")
        elif response.getlayer(TCP).flags == 0x14:
            logging.info(f"Port {port} is closed.")
    else:
        logging.debug(f"Port {port} is in an unknown state.")

# Function to ask for user inputted IP, ping and if open call port scanning function - produces warning if blocking/unresponsive.
def ping_and_scan():
    target_ip = input("Enter the target IP address: ")

    response = sr1(IP(dst=target_ip) / ICMP(), timeout=1, verbose=0)

    if response is None:
        logging.warning(f"Host {target_ip} is down or unresponsive.")
    elif int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
        logging.warning(f"Host {target_ip} is actively blocking ICMP traffic.")
    else:
        logging.info(f"Host {target_ip} is responding.")
        port_scan(target_ip)

# Function to prompt user for port range and call port scan function
def port_scan(host):
    port_range_str = input("Enter the port range (e.g., 20-80): ")
    start_port, end_port = map(int, port_range_str.split("-"))
    port_range = range(start_port, end_port + 1)

    for port in port_range:
        scan_port(host, port)

if __name__ == "__main__":
    # starts logging, then runs the main function 
    setup_logging_file()
    logging.info("Starting the script execution.")
    ping_and_scan()
    logging.info("Script execution completed.")

# End