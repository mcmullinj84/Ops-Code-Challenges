#!/usr/bin/env python3

# Script Name:                  ops301d8-day07
# Author:                       Jonathan McMullin
# Date of latest revision:      06/07/2023
# Purpose:                      Practice python os.walk command

# Declaration of variables

# Declaration of functions

# Main
import os

#this function takes a user input file path and breaks it into root,
# dirs, files using os.walk. It prints out each respective category

def generate_directory_structure(file_path):
    for (root, dirs, files) in os.walk(file_path):
        print("==root==")
        print(root)
        print("==dirs==")
        print(dirs)
        print("==files==")
        print(files)

#this runs previous function with user input

def main():
    user_input = input("Enter a file path: ")
    generate_directory_structure(user_input)

# This ensures the main function is only called if the script is run directly.
# - Credit to Chat GPT for this conditional

if __name__ == "__main__":
    main()

#end