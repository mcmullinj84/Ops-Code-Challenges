#!/usr/bin/env python3 

# Script Name:                  ops401d8-day16
# Author:                       Jonathan McMullin
# Date of latest revision:      07/31/2023
# Purpose:                      Automated Brute Force Wordlist Attack Tool

# 
import time

def iterator():
    # Ask the user for the filepath to the wordlist
    filepath = input("Input the complete filepath for the wordlist: ")

    # Open the wordlist file using the 'with' statement to ensure proper file handling
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

def password_recognized():
    user_input = input("Enter a string: ")
    filepath = input("Input the complete filepath for the wordlist: ")

    try:
        with open(filepath, 'r') as file:
            wordlist = [line.strip() for line in file]

            if user_input in wordlist:
                print("Password recognized.")
            else:
                print("Password not recognized.")
    except FileNotFoundError:
        print("File not found. Please check the filepath.")

def main():
    print("Select a mode:")
    print("Mode 1: Offensive; Dictionary Iterator")
    print("Mode 2: Defensive; Password Recognized")

    mode = input("Enter the mode number (1 or 2): ")

    if mode == "1":
        iterator()
    elif mode == "2":
        password_recognized()
    else:
        print("Invalid mode selection.")

if __name__ == "__main__":
    main()

# End