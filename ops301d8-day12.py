#!/usr/bin/env python3

# Script Name:                  ops301d8-day12
# Author:                       Jonathan McMullin
# Date of latest revision:      06/14/2023
# Purpose:                      Practice python requests

# Note: to install requests package run the following commands in the terminal:
# <sudo apt-get update -y>
# <sudo apt-get install -y python3-requests>

import requests

# Prompt the user for the destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP method
print("Select an HTTP method:")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")
print("5. HEAD")
print("6. PATCH")
print("7. OPTIONS")
choice = input("Enter your choice (1-7): ")

# Map user's choice to the corresponding HTTP method
http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
method = http_methods[int(choice) - 1]

# Print the request information
print("\nRequest:")
print("URL:", url)
print("Method:", method)

# Ask the user for confirmation before proceeding
confirmation = input("Do you want to proceed with the request? (y/n): ")
if confirmation.lower() != "y":
    print("Request cancelled.")
    exit()

# Perform the request using the selected HTTP method
response = requests.request(method, url)

# Print the response status code and translated message
status_code = response.status_code
print("\nResponse:")
print("Status Code:", status_code)

# Translate the status code into plain terms
status_messages = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}

if status_code in status_messages:
    message = status_messages[status_code]
    print("Message:", message)

# Print the response headers
print("\nResponse Headers:")
for header, value in response.headers.items():
    print(header + ":", value)

# Exit