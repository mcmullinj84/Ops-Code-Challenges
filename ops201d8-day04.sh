#!/bin/bash

# Script Name:                  Class 04
# Author:                       Jonathan McMullin
# Date of latest revision:      04/27/2023
# Purpose:                      Testing Arrays

# Declaration of variables

dir_array=("dir1" "dir2" "dir3" "dir4")
# Declaration of functions

#Main
#Here is the function to create all 4 directories
mkdir ${dir_array[*]}

#these lines should create a new text file in each directory.

touch /home/jmc/${dir_array[0]}/anewtext.txt
touch /home/jmc/${dir_array[1]}/anewtext.txt
touch /home/jmc/${dir_array[2]}/anewtext.txt
touch /home/jmc/${dir_array[3]}/anewtext.txt
# End