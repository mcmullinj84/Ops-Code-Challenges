#!/bin/bash

# Script Name:                  output syslog to dated file
# Author:                       Jonathan McMullin
# Date of latest revision:      05/31/2023
# Purpose:                      append date/time

# Declaration of variables
# Define the source file path
source_file="/var/log/syslog"

# Generate the date and time suffix using the format %m-%d-%Y
date_suffix=$(date +"%m-%d-%Y")
# Declaration of functions


# Main

# Create the destination filename with the date suffix
destination_file="syslog_${date_suffix}.log"

# Copy the source file to the destination file
cp "$source_file" "$destination_file"

echo "Copied $source_file to $destination_file"

# End