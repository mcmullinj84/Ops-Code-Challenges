#!/usr/bin/env python3

# Script Name:                  ops301d8-day09
# Author:                       Jonathan McMullin
# Date of latest revision:      06/09/2023
# Purpose:                      Practice python Conditionals

# Declaration of variables
a = 25
b = 30
weather = "sunny"
temperature = 25
# Declaration of functions

def mathquiz():
    #this is a counter
    true_answers = 0 

    if a == b:
        print("The math works.")
        true_answers += 1
    else: print("That's not right.")

    if a != b:
        print("The math works.")
        true_answers += 1
    else: print("That's not right.")

    if a < b:
        print("The math works.")
        true_answers += 1
    else: print("That's not right.")

    if a <= b:
        print("The math works.")
        true_answers += 1
    else: print("That's not right.")

    if a > b:
        print("The math works.")
        true_answers += 1
    else: print("That's not right.")

    if a >= b:
        print("The math works.")
        true_answers += 1
    else: print("That's not right.")

    total_questions = 6
    print ("number of true answers: ", true_answers)
    print ("Total questions: ", total_questions)

    if true_answers <= 0.6 * total_questions:
        print ("You Failed the Quiz")
    elif true_answers == total_questions:
        print ("Perfect Score")
    else: print ("You Passed This Time")

# Main

mathquiz ()


weather = "sunny"
temperature = 25

if weather == "sunny" and temperature >= 20:
    print("The weather is great for a run! Go outside and enjoy your workout.")
elif weather == "cloudy" or temperature < 20:
    print("The weather might not be ideal, but you can still go for a run if you're up for it.")
else:
    print("The weather conditions are not suitable for a run. Consider an indoor workout instead.")


# End