#!/usr/bin/env python3

# Script Name:                  ops401d8-day03
# Author:                       Jonathan McMullin
# Date of latest revision:      07/12/2023
# Purpose:                      Uptime Sensor Tool w/ Email Alert

# import Libraries
import os
import datetime
import time
import smtplib
from email.message import EmailMessage
from getpass import getpass


# Main 
# Transmit a single ICMP (ping) packet to a specific IP.
# Evaluate the response as success/failure. 0 = success
# Credit to ChatGPT for helping with line 18 - to send output to null device
def ping(host):
    response = os.system("ping -c 1 " + host + " > /dev/null 2>&1")
    return response == 0

# prints the status and timestamp for destination IP tested
def print_status(timestamp, host, status):
    print(f"[{timestamp}] Host: {host} - Status: {'Success' if status else 'Failure'}")
# Creates infinite loop with 2 second delay
def uptime_sensor(host):
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = ping(host)
        print_status(timestamp, host, status)
        time.sleep(2)

#input host IP and run loop
host_to_check = "8.8.8.8"
uptime_sensor(host_to_check)