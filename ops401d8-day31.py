#!/usr/bin/env python3

# Script Name:                  ops401d8-day31
# Author:                       Jonathan McMullin
# Date of latest revision:      08/21/2023
# Purpose:                      File Search Tool - Linux + Win

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Import Libraries 

import os, time 
import platform

# Define Functions

def search_files(filename, directory):
    searched_files = 0
    hits = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if filename.lower() in file.lower():
                # Adds to hit count if file name is found
                hits += 1
                file_path = os.path.join(root, file)
                print(f"Found: {file_path}")
            # Adds to file count after each iteration
            searched_files += 1

    return searched_files, hits

# Main 

if __name__ == "__main__":
    filename = input("Enter a file name to search for: ")
    directory = input("Enter the directory to search in: ")

    if platform.system() == "Linux":
        # On Ubuntu Linux
        searched_files, hits = search_files(filename, directory)
    elif platform.system() == "Windows":
        # On Windows 10
        # Convert the directory path to Windows format
        directory = directory.replace("/", "\\")
        searched_files, hits = search_files(filename, directory)
    else:
        print("Unsupported operating system.")
        searched_files = 0
        hits = 0


# Prints number of files/hits
    print(f"Files searched: {searched_files}")
    print(f"Hits found: {hits}")
    print("Search Complete")

# End