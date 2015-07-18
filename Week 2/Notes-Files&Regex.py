import os
__author__ = 'winnie'


# Some basic python os commands

# import os
# print os.getcwd()
# os.mkdir("mydirectory")
# os.chdir("mydirectory") --> goes inside the directory we just made

# os.listdir('.')  --> the period stands for cwd
#
# def create_directoies(list):
#     for x in list:
#         os.mkdir(x)
#
#
#
# def create_nested_directories(list):
#     for x in list:
#         os.mkdir(x)
#         os.chdir(x)
#
# create_nested_directories(["nested_dir1", "nested_dir2", "nested_dir3"])

###################
##     REGEX     ##
###################


# Repetition
# Things get more interesting when you use + and * to specify repetition in the pattern
# + 	1  or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
# * 	0 or more occurrences of the pattern to its left
# ? 	0 or 1
# {4}   4 or more.  r'\d{4}' returns 4 number digits
# {3,}  3 or more
# {3,5} 3, 4, or 5


# Character Classes
# Character Classes match a selection of characters at once. The most common are:
#
# \d	matches any digit from 0 to 9 inclusive
# \w 	matches letters and digits or underbar [a-zA-Z0-9_]
# \W	matches everything but letters and digits
# \s	matches a single whitespace character (space, newline, return, tab, form)
# \n\r\t	newline, return, tab
# \f	form
# \S	matches any non-whitespace character


################
#   EXAMPLES   #
################

# Regex
# Read and Write file
# Read and Write CSV

################
#   REGEX      #
################

import re
# website = "You should check out stackoverflow.com"
# print re.findall(r'\w+.com', website)


# signup_info = "Jenny: jenny@gmail.com, 867-5309"
# email = re.findall(r'\w+@\w+\.com', signup_info)
# name = re.findall(r'\w+', signup_info)
# number = re.findall(r'\d+-\d+', signup_info)
#
# print email, name, number

# emails = ["r.mutter@gmail.com", "r.mutter@yahoo,com", "r.mutteratgmail.com"]
# print filter(lambda x: re.findall(r'\w+@\w+\.com', x) , emails)


##################
#   WRITE FILES  #
##################

# def scraper(file_name):
#     with open('write_file.txt', 'w') as write_file:
#         with open(file_name, 'r') as file:
#             sentences = re.findall(r'\>(.+)\<', file.read())
#             for sentence in sentences:
#                 write_file.write(sentence + "\n")
#
# scraper('blog.html')

# Question, topic, difficulty, answer to question
# import csv
# import random
# def choose_questions(questions, topic, difficulty):
#     with open('write_file.txt', 'w') as write_file:
#         with open('quiz.csv', 'rb') as file:
#             quiz = [row for row in csv.reader(file)]
#             random.shuffle(quiz)
#             count_questions = 0
#             while len(quiz)>1 and count_questions < questions:
#                 question = quiz.pop()
#                 if question[1] == topic and int(question[2]) <= difficulty:
#                     write_file.write(question[0] + "\n")
#                     count_questions +=1
#
# print choose_questions(3, "History", 3)

# import csv
# lines = [
#     ['first column', 'second column'],
#     ['one fish', 'two fish'],
#     ['red fish', 'blue fish']
# ]
# with open('seuss.csv', 'wb') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(lines)

# import csv

# def list_of_powers(number):
#     list = []
#     for x in range(1,6):
#         list.append(number**x)
#     return list


# def create_powers_csv(num_list, powers):
#     lines = [
#         ['1st', '2nd', '3rd', '4th', '5th']
#     ]

#     with open('powers.csv', 'wb') as file:
#         for number in num_list:
#             # or
#             # powers = [number**x for x in range(1,6)]
#             powers = list_of_powers(number)
#             lines.append(powers)
#         csv_writer = csv.writer(file)
#         csv_writer.writerows(lines)
#         print lines


# create_powers_csv([1, 2, 3], 5)
