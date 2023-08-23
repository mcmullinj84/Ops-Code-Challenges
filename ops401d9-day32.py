#!/usr/bin/env python3

# Script Name:                  ops401d8-day31
# Author:                       Jonathan McMullin
# Date of latest revision:      08/22/2023
# Purpose:                      New File Search Tool - Linux + Win

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script

# Import Libraries 

import os
import time
import platform
import hashlib

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
    try:
        file_size = os.path.getsize(file_path)
        file_mtime = time.ctime(os.path.getmtime(file_path))
        return file_size, file_mtime
    except Exception as e:
        print(f"Error getting file info for {file_path}: {str(e)}")
        return None, None

def search_files(filename, directory):
    searched_files = 0
    hits = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if filename.lower() in file.lower():
                hits += 1
                file_path = os.path.join(root, file)
                file_size, file_mtime = get_file_info(file_path)

                if file_size is not None and file_mtime is not None:
                    file_hash = hash_file(file_path)
                    print(f"Found: {file_path}")
                    print(f"Timestamp: {file_mtime}")
                    print(f"File Name: {file}")
                    print(f"File Size: {file_size} bytes")
                    print(f"MD5 Hash: {file_hash}")
                    print("-" * 40)

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

    print(f"Files searched: {searched_files}")
    print(f"Hits found: {hits}")