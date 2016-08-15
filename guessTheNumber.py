

##this program prints out a lucky number between 1 and 20

import random

secretNumber = random.randint(1, 20);

print("I'm thinking of a number between 1 and 20.");

#ask the player to guess the number six times

for guessNumber in range (1, 7):
    print ("Guess taken.");
    
    guess = int(input());

    if guess <secretNumber :
        print ("The guess is too low");

    elif guess >secretNumber :
        print ("The guess is too high.");

    else:
        break; # this condition is the correct guess!

if guess == secretNumber :
    print("Good job! You guessed my number in " + str(guessNumber) + " guesses!");

else:
    print ("Nope. The number I was thinking of was " + str(secretNumber));
        
