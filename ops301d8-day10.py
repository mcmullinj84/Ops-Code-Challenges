#!/usr/bin/env python3

# Script Name:                  ops301d8-day10
# Author:                       Jonathan McMullin
# Date of latest revision:      06/09/2023
# Purpose:                      Practice python File Handling

# Declaration of variables

# Declaration of functions

# Main 

file_name = "PythonTest.txt"
file = open(file_name, "w")

# Appends three lines to the file
lines = ["This is line 1", "This is line 2", "This is line 3"]
for line in lines:
    file.write(line + "\n")

# Closes the file
file.close()

# Opens the file again to read the first line
file = open(file_name, "r")
first_line = file.readline()

# Prints the first line
print("First line:", first_line)

# Close the file
file.close()

# Delete the file
import os
os.remove(file_name)

print("File Deleted")

# End 