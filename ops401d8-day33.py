#!/usr/bin/env python3

# Script Name:                  ops401d8-day33
# Author:                       Jonathan McMullin
# Date of latest revision:      08/24/2023
# Purpose:                      TotalVirus Enabled File Search Tool - Linux + Win

# Credit: Utilized syntax from Code Fellows Demo and ChatGPT to develop this script
# This uses the VirusTotal API and a script written by eduardxyz named "virustotal-search.py"

# Import Libraries

import os
import hashlib
import time
import requests

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

def check_virustotal_file(hash_value, api_key, output_file):
    parameters = {"apikey": api_key, "resource": hash_value}
    url = requests.get("https://www.virustotal.com/vtapi/v2/file/report", params=parameters)
    json_response = url.json()
    response = int(json_response.get("response_code"))

    if response == 0:
        print(hash_value + ": UNKNOWN")
        with open(output_file, "a") as file:
            file.write(hash_value + " 0\n")
    elif response == 1:
        positives = int(json_response.get("positives"))
        if positives >= 3:
            print(hash_value + ": MALICIOUS")
            with open(output_file, "a") as file:
                file.write(hash_value + " " + str(positives) + "\n")
        else:
            print(hash_value + ": NOT MALICIOUS")
            with open(output_file, "a") as file:
                file.write(hash_value + " 0\n")
    else:
        print(hash_value + ": CAN NOT BE SEARCHED")

def check_virustotal_hash(api_key, hash_values, output_file, premium=False):
    for hash_value in hash_values:
        check_virustotal_file(hash_value, api_key, output_file)
        if premium:
            time.sleep(1)
        else:
            time.sleep(16)

def virustotal_menu(api_key):
    while True:
        print("\nVirusTotal Menu:")
        print("1. Check Single Hash")
        print("2. Check Hashes from File")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            hash_value = input("Enter the SHA-1 hash to check against VirusTotal: ")
            check_virustotal_file(hash_value, api_key, "virustotal_results.txt")
        elif choice == "2":
            input_file = input("Enter the file containing SHA-1 hashes to check: ")
            premium = input("Use premium mode? (y/n): ").lower() == 'y'
            with open(input_file, "r") as file:
                hash_values = [line.strip() for line in file.readlines()]
                check_virustotal_hash(api_key, hash_values, "virustotal_results.txt", premium)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Main

if __name__ == "__main__":
    api_key = os.getenv("apikey")
    if not api_key:
        print("API key not found. Make sure you set the 'apikey' environmental variable.")
    else:
        while True:
            print("\nMain Menu:")
            print("1. Recursive Search for Files")
            print("2. VirusTotal Hash Check")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                directory = input("Enter an absolute directory path to search in: ")
                if not os.path.exists(directory):
                    print("Directory does not exist.")
                else:
                    searched_files, total_scanned = search_files(directory)
                    print(f"Files searched: {searched_files}")
                    print(f"Total files scanned: {total_scanned}")
            elif choice == "2":
                virustotal_menu(api_key)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

# End