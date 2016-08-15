
##prints a random number between 1 and 8

import random

def getNumber(number):
    if number == 1:
        return "One is a your lucky number!";
    
    elif number ==2:
        return "Two! you got it!";

    elif number == 3:
        return "Three !Go son!";

    elif number ==4 :
        return "Four! It's your lucky day!";

    elif number == 5:
        return "Five! Stay calm and python forward!";

    elif number ==6:
        return "Six! Wow...you getting it!";

    elif number == 7:
        return "Seven! The seventh day of the week!";

    elif number == 8:
        return " Eight! You are smart!!";

    elif number == 9:
        return "You're a python expert! At cloud nine!";

num = random.randint(1,9);
lucky = getNumber(num);
print(lucky);
        
