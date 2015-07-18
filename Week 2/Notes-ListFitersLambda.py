__author__ = 'winnie'

######################
# List comprehension #
######################

# List comprehensions provide a concise way to create lists.
# Instead of writing something like this:
# new_list = []
# for number in array:
#     new_list.append(number * 2)

# print [word.lower() for word in ["Try", "tHiS", "OUT"]]
# print [number ** 2 for number in [1, 2, 3, 4, 5]]
# print [(temp - 32) * 5/9 for temp in [104, 32, 68]]

# # I can print out list dictionaries:
# dict = {"key1": "value1", "key2": "value2"}
# print [word.capitalize() for word in dict.values()]
#
# # I can even put logic in my list comprehension
# print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#
# # Nested list comprehensions
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],]
# print [[row[i] for row in matrix] for i in range(4)]


###############
#   FILTERS   #
###############

# Filter definition:
# filter(function, iterable input)

# new_list = []
# for number in [0, -3, 5, 8, -7]:
#     if number > 0:
#         new_list.append(number)
#
# def positive(x):
#     return x >= 0
#
# new_list = filter(positive, [0, -3, 5, 8, -7])
#
# print new_list

# def length(word):
#     return len(word)>3
#
# print filter(length, ["Some", "words", "to", "test"])
#
#
# def even(num):
#     return num%2 == 0
#
# print filter(even, [1, 2, 3, 4, 5])
#
#
# class RaceCar(object):
#     def __init__(self, color):
#         self.color = color
#
#     def __repr__(self):
#         return self.color
#
# def red(word):
#     return word.color != 'red'
#
# print filter(red, [RaceCar("black"), RaceCar("blue"), RaceCar("red")])

###############
#   LAMBDA    #
###############

# Lambda reduces necessity of writing a function for filter by anonymizing functions:
    # function(x) --> return x + 1
    # lambda x: x+1
# filter( lambda input: return , iterable input )

# print filter(lambda x: x%2==0, [1, 2, 3, 4, 5])
#
# print filter(lambda x: len(x)>3, ["Some", "words", "to", "test"])

# people = [
#     ('Jack', 35),
#     ('Jill', 23),
#     ('Betty', 50)
# ]
#
# print people
#
# print sorted(people, key=lambda person: person[1])

# print filter(lambda x: x%3 ==0 , [6, 8, 11, 12, 15])
# print filter(lambda word: word[0].islower(), ["Todd", "jane", "George"])

# toppings = [('meat lovers', ['sausage', 'pepperoni', 'bacon', 'ham']),
#             ('cheese', ['cheese']), ('veggie', ['mushrooms', 'onion', 'peppers'])]
#
# print sorted(toppings, key = lambda topping: len(topping[1]), reverse = True)

##################
#   DECORATORS   #
##################
# @classmethod, and @staticmethod are examples of decorators.
# They wrap our functions and can modify or edit the output.
# Decorators typically pass in inner() functions
#
# def currency(function):
#     def inner(x):
#         return "${:.2f}".format(function(x))
#     return inner
#
# @currency
# def money(x):
#     return x
#
# @currency
# def with_tips(x):
#     return x * 1.15
#
# print with_tips(4)
# print money(4)

##################
#   GENERATORS   #
##################


# def evens():
#     i = 1
#     count = 1
#     while count<=10:
#         if i % 2 == 0:
#             yield i
#             count += 1
#         i = i + 1
#
# for int in evens():
#     print int
#
#
# def double():
#     i = 1
#     while i<1000:
#         yield i
#         i *= 2
#
# for int in double():
#     print int


# import string
# import random
#
# def printaz():
#     azlist = list(string.ascii_lowercase)
#     random.shuffle(azlist)
#     while len(azlist)>0:
#         letter = azlist.pop()
#         yield letter
#
# for x in printaz():
#     print x

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print factorial(3)


#########################################
# Filter, Map, Reduce Practice Problems #
#########################################

# start_list = [5, 3, 1, 2, 4]

# square_list = []

# for i in start_list:
# 	square_list.append(i ** 2)

# print sorted(square_list)

# print filter(lambda x: x > 2, start_list)
# print map(lambda x: x**2, start_list)
# print reduce(lambda x, y: x + y, start_list) # Incrementally adds all numbers up together

# List comprehensions are really cool
# def evens_to(number):
# 	# THis is a much better way of doing things:
# 	# return [i for i in range(30) if not i%2]
# 	arr = []
# 	for i in range(30):
# 		if not i%2: arr.append(i)
# 	return arr

# print evens_to(30)	

# cubes_by_four = [x**3 for x in range(1,11) if not (x**3)%4]
# print cubes_by_four

# cubes_again = [x**3 for x in range(1,11)]
# print cubes_again[1::2]  # print every other number
# print cubes_again[::-1]  # or print it backwards

# def digit_sum(n):
# 	return reduce(lambda x, y: x + y, map(int, str(n)))

# print digit_sum(123)

# def reverse(text):
#     str = ""
#     for i in range(len(text)):
#         str += text[len(text)-i-1]
#     return str


# print reverse("hello")

# def anti_vowel(text):
#     letters = filter(lambda x: x.lower() not in ["a", "e", "i", "o", "u"], list(text))
#     return ("").join(letters)

# print anti_vowel("There are no words for this")


# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
#          "x": 8, "z": 10}

# def scrabble_score(word):
# 	total = 0
# 	for i in word.lower():
# 		try:
# 			total += score[i]
# 		except:
# 			total += 0
# 	return total

# print scrabble_score("wordZ")

# If there are no spaces in a word, you can also do something like this:
# print sum(map(lambda x: score[x], "wordZ".lower()))



