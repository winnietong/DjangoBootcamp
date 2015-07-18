__author__ = 'winnie'
from random import randint

def get_answer(n1, n2, type):
    try:
        ans = int(raw_input("What's {} {} {}? ".format(n1, type, n2)))
        return ans
    except:
        print "Please enter an integer!"
        return get_answer(n1, n2, type)

def get_questions(num_questions, levels, types):
    correct = 0
    operands = {"B": 10, "I": 24, "A": 100}
    types_dictionary = {"A": "+", "S": "-", "M": "*"}

    for i in range(num_questions):
        n1 = randint(1, operands[levels])
        n2 = randint(1, operands[levels])

        if types == "MI":
            random_num = randint(0,2)
            type = types_dictionary.values()[random_num]
        else:
            type = types_dictionary[types]

        expression = "{} {} {}".format(n1, type, n2)
        prod = eval(expression)
        ans = get_answer(n1, n2, type)

        if ans == prod:
            print "That's right -- well done.\n"
            correct = correct + 1
        else:
            print "No, I'm afraid the answer is {}.\n".format(prod)
    return correct

def game():
    try:
        num_questions = int(raw_input("How many questions would you like? "))
    except:
        print "Please type in an integer!"
    else:
        levels = raw_input("(B)eginner, (I)ntermediate or (A)dvanced? ").upper()
        types = raw_input("(A)ddition, (S)ubtraction, (M)ultiplication or (MI)xed? ").upper()

        correct = get_questions(num_questions, levels, types)

        print "I asked you {} questions.  You got {} of them right.".format(num_questions, correct)
        percent_correct = float(correct)/float(num_questions)
        if percent_correct > 2.0/3.0:
            print "Well done!\n"
        elif percent_correct > 1.0/3.0:
            print "You need more practice\n"
        else:
            print "Please ask your math teacher for help!\n"
    game()

game()
