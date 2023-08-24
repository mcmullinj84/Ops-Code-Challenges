#!/usr/bin/env python3

# Script Name:                  ops401d8-day31
# Author:                       Jonathan McMullin
# Date of latest revision:      08/24/2023
# Purpose:                      TotalVirus Enabled File Search Tool - Linux + Win

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Import Libraries


import os
import hashlib
import time

# Define Functions

def hash_file(filename):
    """This function returns the SHA-1 hash of the file passed into it"""
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        data = file.read(1024)
        while data:
            h.update(data)
            data = file.read(1024)
    return h.hexdigest()

def get_file_info(file_path):
    #This function uses os to get the size + timestamp
    try:
        file_size = os.path.getsize(file_path)
        file_mtime = os.path.getmtime(file_path)
        return file_size, file_mtime
    except Exception as e:
        print(f"Error getting file info for {file_path}: {str(e)}")
        return None, None

def format_timestamp(timestamp):
    # This function turns the timestamp into a human readable format
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

def search_files(directory):
    # sets counter to 0
    searched_files = 0

    # Uses os.walk to recursively iterate through user input directory
    # and generate file paths.
    for root, _, files in os.walk(directory):
        for file in files:
            # os.path.join allows the script to run on both ubuntu and windows
            file_path = os.path.join(root, file)
            file_size, file_mtime = get_file_info(file_path)

            if file_size is not None and file_mtime is not None:
                file_hash = hash_file(file_path)
                print(f"File Path: {file_path}")
                print(f"Timestamp: {format_timestamp(file_mtime)}")
                print(f"File Name: {file}")
                print(f"File Size: {file_size} bytes")
                print(f"SHA-1 Hash: {file_hash}")
                print("-" * 40)

            searched_files += 1

    return searched_files

# Main

if __name__ == "__main__":
    directory = input("Enter an absolute directory path to search in: ")
    
    if not os.path.exists(directory):
        print("Directory does not exist.")
    else:
        searched_files = search_files(directory)

        print(f"Files searched: {searched_files}")