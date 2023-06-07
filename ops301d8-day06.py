#!/usr/bin/env python3

# Script Name:                  Bash in Python
# Author:                       Jonathan McMullin
# Date of latest revision:      06/06/2023
# Purpose:                      Practice python using bash scripts

# Declaration of variables

# Declaration of functions

# Main

# The os module in Python is a built-in module that provides a way to interact with the 
# operating system.
# It gives you Python code that is capable of interacting with the underlying operating system,
# enabling you to perform tasks related to file management, process handling, environment 
# manipulation, and system information retrieval - credit CODEFELLOWS

import os

# The `os.system()` function in Python executes a shell command and returns the exit status 
# of the command as an integer value.
# Here we assigned desired outputs to variables

user = os.system("whoami")
ip =  os.system("ip a")
hardware = os.system("lshw -short")

# if you print the variable, you get a 0 or a 1
print(user)

print(ip)

print(hardware)

print("0's = successful operation")

# End
