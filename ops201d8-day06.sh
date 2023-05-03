#!/bin/bash

# Script Name:                  ops201d8-day06
# Author:                       Jonathan McMullin
# Date of latest revision:      05/01/2023
# Purpose:                      Practice Conditonals

# Declaration of variables
#empty array to store file names
new_files=()



# Declaration of functions 
# Define a function to check for the existence of a file or directory
check_file_or_dir() {
  if [ -e "$1" ]
  then
    echo "The file $1 exists in the current directory."
  elif [ -d "$1" ]
  then
    echo "The directory $1 exists in the current directory."
  else
    echo "The file/directory $1 does not exist in the current directory. Creating new file..."

    # Create a new text file with the input filename
    touch "$1.txt"
    echo "New file $1.txt created."

    # Add the name of the new file to the array
    new_files+=("$1.txt")
  fi
}
# Main

# loop to keep the script running if there are under 100 files
# current directory
while [ $(ls | wc -l) -lt 100 ]
do
  # Ask the user to input the filename
  echo "Enter the filename to check:"
  read filename

  # Input filename into checking function
  check_file_or_dir "$filename"

  # Print the new_files array after each time the user enters a filename
  echo "New files created by the script:"
  # Checks if the number of new files is greater than 0
  if [ ${#new_files[@]} -gt 0 ]
  then
    for file in "${new_files[@]}"
    do
      echo "$file"
    done
  else
    echo "No new files were created by the script."
  fi
done

echo "There are now 100 or more files in the current directory. Work Complete."

#End