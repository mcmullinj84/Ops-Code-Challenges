#!/bin/bash

# Script Name:                  ops201d8-day13
# Author:                       Jonathan McMullin
# Date of latest revision:      05/10/2023
# Purpose:                      Domain Analyzer

# Declaration of variables

# Declaration of functions
DomainAnalysis () {
#This function calls the 4 commands to below to provide info based
#on the domain input by the user
whois $1
dig $1
host $1
nslookup $1
}

# Main
#This requests the user to input a domain name
echo "Enter Domain To Receive OSINT"
read userinput
#This calls the function and output the information into a .txt file
#on the user's 'home' directory
DomainAnalysis "$userinput" >> ~/DomainOSINT.txt
#This opens the file in a terminal text editor
nano ~/DomainOSINT.txt

# End