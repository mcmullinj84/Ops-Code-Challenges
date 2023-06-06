#!/bin/bash

# Script Name:                  Backup, Compress, and Clear Syslogs
# Author:                       Jonathan McMullin
# Date of latest revision:      06/06/2023
# Purpose:                      Practice back up syslogs, compress, and clear

# Declaration of variables
 
# establishes the path to backup directory
backup_dir="$HOME/backups-syslogs"

#establishes timestamp
timestamp=$(date +"-%Y%m%d%H%M%S")

# Declaration of functions

#This Function checks for a backup directory and creates one if needed
CheckDir () {
while [ ! -d "$backup_dir" ]; do
    echo "Creating backup directory: $backup_dir"
    mkdir -p "$backup_dir"
done

echo "Backup directory exists: $backup_dir"
}

# Main

CheckDir

# prints size of syslogs
syslog_size=$(du -h /var/log/syslog | awk '{print $1}')
echo "Size of /var/log/syslog: $syslog_size"

# prints the size of wtmp
wtmp_size=$(du -h /var/log/wtmp | awk '{print $1}')
echo "Size of /var/log/wtmp: $wtmp_size"

# Compress the log files into a single zip file with timestamp suffix
zip_filename="syslogs${timestamp}.zip"
zip -r "$backup_dir/$zip_filename" /var/log/syslog /var/log/wtmp

# Clear the contents of the original log files
sudo truncate -s 0 /var/log/syslog
sudo truncate -s 0 /var/log/wtmp

echo "Contents of syslog and wtmp cleared"

# Prints the size of the compressed file
compressed_size=$(du -h "$backup_dir/$zip_filename" | awk '{print $1}')
echo "Size of compressed file ($zip_filename): $compressed_size"

# Prints the size of the original log files for comparison
echo "Size of /var/log/syslog before compression: $syslog_size"
echo "Size of /var/log/wtmp before compression: $wtmp_size"

# End