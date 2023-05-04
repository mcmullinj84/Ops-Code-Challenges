# Script Name:                  #ops201d8-day08.bat
# Author:                       Jonathan McMullin
#Date of latest revision:       05/03/2023
# Purpose:                      Practice Batch script

#echo off should help the script run smoothly
@echo off
# Declaration of variables

set desktopPath=C:\Users\j.thompson\desktopPath
set externalDrive=E:\CopyForJorge

# Declaration of functions

# Main

echo Copying files from Desktop to External Drive.

# moves the files from the desktop to the exeternal drive
# mir will make the file a 'mirror', xf excludes the desktop.ini file 
# which can be problematic

robocopy "%desktopPath%" "%externalDrive%\Desktop" /mir /xf "desktop.ini"

echo Copy Complete.

# End