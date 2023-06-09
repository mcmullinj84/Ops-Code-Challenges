#!/usr/bin/env python3

# Script Name:                  ops301d8-day08
# Author:                       Jonathan McMullin
# Date of latest revision:      06/08/2023
# Purpose:                      Practice python lists and slicing

# Declaration of variables

# Declaration of functions

# Main

#This puts the 10 strings into list, stored in a variable
fruits = ["apple", "banana", "orange", "pear", "grape", "kiwi", "melon", "peach", "plum", "mango"]

# This prints the fourth fruit
print("Fourth Fruit:", fruits[3])

print("Sixth Through Tenth Fruits:")
for fruit in fruits[5:10]:
    print(fruit)

fruits[6] = "onion"
print("Updated Seventh Element:", fruits[6])

# End