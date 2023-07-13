#!/usr/bin/env python3

# Script Name:                  ops401d8-day03
# Author:                       Jonathan McMullin
# Date of latest revision:      07/12/2023
# Purpose:                      Uptime Sensor Tool w/ Email Alert

#credit to my instructor Marco for structure for check_ping function

# import Libraries
import os
import datetime
import time
import smtplib
from getpass import getpass

email = input("Enter your email address: ")
# use "app password" not, normal password
password = getpass("Enter your password: ")
ip = input("Enter an IP address: ")
up = "Host in active"
down = "Host is down"

# check status change
last = 0
ping_result = 0 

# Functions 

#Function to handle down alert (change from up to down)
def send_upAlert():
    now = datetime.datetime.now()
    s = smtplib.SMTP("smtp.gmail.com", 587)

    #start TLS
    s.starttls()

    #Authentication
    s.login(email, password)

    message = "Your server is back up"

    # send the email
    s.sendmail("mailbot@codefellows.com", email, message)

    # Close the session
    s.quit()

#Function to handle down alert (change from down to up)
def send_downAlert():
    now = datetime.datetime.now()
    s = smtplib.SMTP("smtp.gmail.com", 587)

    #start TLS
    s.starttls()

    #Authentication
    s.login(email, password)

    message = "Your server is down"

    # send the email
    s.sendmail("mailbot@codefellows.com", email, message)

    # Close the session
    s.quit()


def check_ping():
    now = datetime.datetime.now()
    global ping_result # starts as 0
    global last # starts as 0

    # Sends a single ping to target and puts the response into a variable
    #response = os.system("ping -c 1 " + target)

    # Check the change of ping status from up to down and down to up

    if ((ping_result != last) and (ping_result == up)):
        
        # Change value of last
        last = up
        
        # Calls function to send email
        send_upAlert()

    elif ((ping_result != last) and (ping_result == down)):
        
        # Change value of last
        last = down
        # Calls function to send email
        send_downAlert()
    
    # Ping User inputted IP address and put it into local variable "response" 
    response = os.system("ping -c 1 " + ip)

    # Evaulate the ping response
    if response == 0:
        ping_result = up 
    else:
        ping_result = down

    print(str(now) + ping_result + "to " + ip)

# Main 

# infinite loop

while True: 
    check_ping()
    time.sleep(2)

