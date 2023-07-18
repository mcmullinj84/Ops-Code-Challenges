#!/usr/bin/env python3

# Script Name:                  ops401d8-day06
# Author:                       Jonathan McMullin
# Date of latest revision:      07/17/2023
# Purpose:                      Encryption

# import libraries
from cryptography.fernet import Fernet

# Declare Functions

# Function that handles key generation
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

# Main

# Generate and write the new key
write_key()

# load the generated key
key = load_key()
print("Key is " + str(key.decode('utf-8')))

# Encrypt a message

# message to be encrypted
message = "For Your Eyes Only".encode()

print("Plaintext message is " + message)

# DO THE ENCRYPTION - starts Fernet module and names it "f"

f = Fernet(key)

# Encrypt message
encrypted_message = f.encrypt(message)

# Print the encrypted message
print("The encrypted message is: " + encrypted_message.decode('utf-8'))

