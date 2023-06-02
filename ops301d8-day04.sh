#!/bin/bash

# Script Name:                  Change file permissions
# Author:                       Jonathan McMullin
# Date of latest revision:      06/01/2023
# Purpose:                      practice building a menu

# Declaration of variables

# Declaration of functions

# Main
while true; do
    clear
    echo "Please input the # of the operation you would like"
    echo "1. Hello World"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    read choice

    if [[ $choice == 1 ]]; then
        echo "Hello World"
        # The -p option is used with the read command to display a prompt to the user and wait for them to enter input.
        read -p "Press Enter to continue"
    elif [[ $choice == 2 ]]; then
        ping -c 4 127.0.0.1
        read -p "Press Enter to continue"
    elif [[ $choice == 3 ]]; then
        ip a
        read -p "Press Enter to continue"
    elif [[ $choice == 4 ]]; then
        echo "Exiting"
        exit 0
    else
        echo "Invalid choice"
        read -p "Press Enter to continue"
    fi
done