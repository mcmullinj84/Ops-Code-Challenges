#!/bin/bash

# Script Name:                  ops201d8-day05.sh
# Author:                       Jonathan McMullin
# Date of latest revision:      04/28/2023
# Purpose:                      Practice Loop and use PID features

# Declaration of variables
input=()
# Declaration of functions

# Main
while true; do
ps aux
echo "Above is active PIDs, input PID # to kill or press Ctrl+C to end"
read input
kill $input
echo "PID $input neutralized"
done    
#echo 

# End