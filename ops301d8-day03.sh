#!/bin/bash

# Script Name:                  Change file permissions
# Author:                       Jonathan McMullin
# Date of latest revision:      06/01/2023
# Purpose:                      practice changing file permissions in a script

# Declaration of variables
UserInputDirPath=()
UserInputPer=()

# Declaration of functions

# Main
# prompts user for desired directory and permissions number, stores as variable

read -p "Input Directory Path to Change Permissions: " UserInputDirPath

read -p "Input Permissions Number: " UserInputPer

# changes permissions according to user inputs recursively

chmod -R "$UserInputPer" "$UserInputDirPath"

# Prints the Directory with new permissions
echo "New Permissions"
ls -l "$UserInputDirPath"

# End