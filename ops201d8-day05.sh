#!/bin/bash

# Script Name:                  Print Hello Worldp
# Author:                       Jonathan McMullin
# Date of latest revision:      04/28/2023
# Purpose:                      Practice Loop and use PID features

# Declaration of variables
PID=$(ps)
input=()
# Declaration of functions

the_loop (){
while [[ $PID != 0 ]]
do
    echo "Above is active PIDs, input PID # to kill"
    read input
    kill $input var=$((var+1))
    echo "PID $input neutralized"
    echo $PID
done    
}
# Main
echo 
echo $PID
echo
the_loop
echo "PID killing complete"

#echo 

# End