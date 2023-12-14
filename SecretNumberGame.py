#Secret Number Guessing Game

import random

print('Hello. What is your name')
name = input()

print('Nice to meet you, ' + name + '. I am thinking of a secret number from 1-20.')
print('Can you guess it? You will have 5 tries.')

secretNumber = random.randint(1,20)

#print('DEBUG: The secret number is: ' + str(secretNumber))

for guessesTaken in range(1,6):
    print('Take a guess.')
    guess = int(input())
    if guess > secretNumber:
        print('Your guess is too high.')
    elif guess < secretNumber:
        print('Your guess is too low.')
    else:
        break


if guess == secretNumber:
    print('Congratulations! You guessed that the secret number was: ' + str(secretNumber) + '. It only took you ' + str(guessesTaken) + ' tries.')
else:
    print('Sorry. You didn\'t guess the number I was thinking of. The secret number was: ' + str(secretNumber))
