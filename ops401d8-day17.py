#!/usr/bin/env python3 

# Script Name:                  ops401d8-day17
# Author:                       Jonathan McMullin
# Date of latest revision:      08/02/2023
# Purpose:                      Automated Brute Force Wordlist Attack Tool + SSH Authentication

# Used Demo syntax and ChatGPT to develop this script.

# Import Libraries
import paramiko
from getpass import getpass
import time 
# Declare Functions

def iterator():
    # Ask the user for the filepath to the wordlist
    filepath = input("Input the complete filepath for the wordlist: ")

    # Open the wordlist file using the 'with' statement to ensure proper file handling (Chat GPT Recommended)
    with open(filepath, 'r') as file:
        line = file.readline()
        print(line)

        # While loop to check each line in the wordlist
        while line:
            # Remove empty space from the line
            line = line.rstrip()
            word = line
            print(word)
            time.sleep(1)

            # Get the next line in the wordlist
            line = file.readline()
        file.close()

def password_recognized():
    user_input = getpass("Enter a string: ")
    filepath = input("Input the complete filepath for the wordlist: ")

    # 'Try' runs script as long as no errors occur, 'except' handles the error
    try:
        with open(filepath, 'r') as file:
            wordlist = [line.strip() for line in file]

            if user_input in wordlist:
                print("Password recognized.")
            else:
                print("Password not recognized.")
    except FileNotFoundError:
        print("File not found. Please check the filepath.")

def ssh_authentication():
    host = input("Provide IP address to SSH into: ")
    user = input("Please provide a username: ")
    password = getpass("Input password: ")
    port = 22

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port, user, password)
        stdin, stdout, stderr = ssh.exec_command("whoami")
        time.sleep(3)
        output = stdout.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command("ls -l")
        time.sleep(3)
        output = stdout.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command("pwd")
        time.sleep(3)
        output = stdout.read()
        print(output)
    except paramiko.AuthenticationException:
        print("Authentication Failed")

def main():
    print("Select a mode:")
    print("Mode 1: Offensive; Dictionary Iterator")
    print("Mode 2: Defensive; Password Recognized")
    print("Mode 3: Authenticate to SSH Server")

    mode = input("Enter the mode number (1, 2, or 3): ")

    if mode == "1":
        iterator()
    elif mode == "2":
        password_recognized()
    elif mode == "3":
        ssh_authentication()
    else:
        print("Invalid mode selection.")

# Main 

if __name__ == "__main__":
    main()

# End