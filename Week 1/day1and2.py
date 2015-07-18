__author__ = 'winnie'

# A lot of people have asked me what going through a coding bootcamp was like!
# Good question. Hopefully these notes will help you be prepared or give
# you an understanding of what we have learned since day 1.

##################
# Week 1, Day 1: #
##################

# Dates and strings basics #
###########################

# from datetime import datetime
# now = datetime.now()
#
# print '%s/%s/%s' % (now.year, now.month, now.day)


# def censor(text, word):
# 	return text.replace(word, "*"*len(word))
#
# print censor("this is a hack", "hack")


# Lists Basics #
################

# animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

# # To get the Index and set a new animal
# duck_index = animals.index("duck")
# animals.insert(duck_index, "dog")

# print animals[:3]

# You can also add an interator [start:end:iterator]
# Try it out:

# print animals[::-1]
# print animals[::2]

##################
# Week 1, Day 2: #
##################

# Basic functions and conditionals #
####################################

## Practice problems in class

## Guessing Game
#
# import random
#
# def random_number():
#     return random.randint(0,100)
#
# def check_guess(guess, answer):
#     guesses = 1
#     while (guess != answer):
#         if (guess > answer):
#             guess = int(raw_input("Too high. Try again: "))
#         else:
#             guess = int(raw_input("Too low. Try again: "))
#         guesses += 1
#     return guesses
#
# print "Time to play a guessing game."
# guess = int(raw_input("Enter a number between 1 to 100: "))
# answer = int(random_number())
# guesses = check_guess(guess, answer)
# print "Congratulations! You got it in {} guesses!".format(guesses)

# Calculator problem
#
# def calculator():
#     response = raw_input("What operation would you like to perform (add or subtract)?")
#
#     if response == "add":
#         number_1 = raw_input("First number?")
#         number_2 = raw_input("Second number?")
#         answer = float(number_1) + float(number_2)
#         print answer
#     elif response == "subtract":
#         number_1 = raw_input("First number?")
#         number_2 = raw_input("Second number?")
#         answer = float(number_1) - float(number_2)
#         print answer
#     elif response == "q":
#         print "Thanks for using the calculator!"
#         return
#     else:
#         print "Sorry, didn't understand your response. Try again."
#
#     calculator()
#
# calculator()


# While loop. Baylee's Way

# response = raw_input("What operation would you like to perform (add or subtract)? ")
#
# while response != 'q':
#
#     if response == "add":
#         numbers = raw_input("What numbers would you like to add? (separate w/space) ")
#         numbers = numbers.split(" ")
#         answer = float(numbers[0]) + float(numbers[1])
#         print answer
#         response = raw_input("What operation would you like to perform (add or subtract)? ")
#     elif response == "subtract":
#         numbers = raw_input("What numbers would you like to subtract? (separate w/space) ")
#         numbers = numbers.split(" ")
#         answer = float(numbers[0]) - float(numbers[1])
#         print answer
#         response = raw_input("What operation would you like to perform (add or subtract)? ")
#     else:
#         print "Sorry, didn't understand your response. Try again."
#         response = raw_input("What operation would you like to perform (add or subtract)? ")
#
# print "Thanks for using calculator!"

#Advanced calculator using While Loop
#
# response = ""
#
# def ask_number():
#     number_1 = raw_input("First number? ")
#     number_2 = raw_input("Second number? ")
#     return float(number_1), float(number_2)
#
# while (response != 'q'):
#     response = raw_input("Choose an operation (add, subtract, multiply, divide) or (A)dvanced: ").lower()
#
#     if response == "add":
#         x, y = ask_number()
#         answer = x + y
#         print answer
#     elif response == "subtract":
#         x, y = ask_number()
#         answer = x - y
#         print answer
#     elif response == "multiply":
#         x, y = ask_number()
#         answer = x * y
#         print answer
#     elif response == "divide":
#         x, y = ask_number()
#         answer = x / y
#         print answer
#     elif response == "a":
#         advanced_response = raw_input("(F)ind remainders, (E)xponential functions or (T)aking square roots: ")
#         if advanced_response == "F":
#             x, y = ask_number()
#             answer = x%y
#             print "The remainder of {} into {} is {}".format(x, y, answer)
#         elif advanced_response == "E":
#             x, y = ask_number()
#             answer = x ** y
#             print answer
#         elif advanced_response =="T":
#             x = float(raw_input("Which number do you want the square root of? "))
#             answer = x ** (0.5)
#             print answer
#     elif response == 'q':
#         print "Thanks for using the calculator!"
#     else:
#         print "Sorry, didn't understand your response. Try again."

# juices = [
#     {'name' : 'apple', 'exp_date': 'july'},
#     {'name' : 'grape', 'exp_date': 'august'},
#     {'name' : 'pomegranate', 'exp_date': 'june'},
#     {'name' : 'pineapple'},
#     {'name' : 'orange'}
# ]

# def drink_juice(juice, name):
#     dirty_juice = False
#     for juice in juices:
#         if juice['name'] == name:
#             try:
#                 juice['exp_date']
#             except:
#                 print "{} juice has no expiration date".format(juice['name'])
#                 dirty_juice = True
#             else:
#                 index = juices.index(juice)
#                 juices.pop(index)
#     print juices
#     return dirty_juice
#
# drink_juice(juices, 'pineapple')
