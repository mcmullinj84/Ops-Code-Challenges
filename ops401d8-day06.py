#!/usr/bin/env python3

# Script Name:                  ops401d8-day06
# Author:                       Jonathan McMullin
# Date of latest revision:      07/17/2023
# Purpose:                      Encryption

# Credit: Utilized syntax from the Demo and ChatGPT to develop this script

# import libraries
from cryptography.fernet import Fernet
import os

def write_key():
    # Generate a key and save it to a file
    key = Fernet.generate_key()
    # checks for "key.key", creates it if not existing
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the generated key for encryption/decryption
def load_key():
    # Return the key from the key.key file
    return open("key.key", "rb")

# Function to encrypt a file
def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Function to encrypt a message
def encrypt_message(message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print("The encrypted message is: " + encrypted_message.decode())

# Function to decrypt a message
def decrypt_message(encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    print("The decrypted message is: " + decrypted_message.decode())

# Main
if __name__ == "__main__":
    # Generate and write the new key
    write_key()

    # Load the generated key
    key = load_key().read()
    print("Key is: " + key.decode('utf-8'))

    # Prompt user for mode selection
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

    if mode == 1 or mode == 2:
        # Prompt user for the file path
        file_path = input("Enter the file path: ")

        if mode == 1:
            # Encrypt the target file
            encrypt_file(file_path)
            print("File encrypted successfully.")
        else:
            # Decrypt the target file
            decrypt_file(file_path)
            print("File decrypted successfully.")

    elif mode == 3 or mode == 4:
        # Prompt user for the message
        message = input("Enter the message: ")

        if mode == 3:
            # Encrypt the message
            encrypt_message(message)
        else:
            # Decrypt the message
            decrypt_message(message)
    else:
        print("Invalid mode selection.")
