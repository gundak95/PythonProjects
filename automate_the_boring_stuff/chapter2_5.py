#import random
#print('I am thinking of a number between 1 and 20.')
#answer = random.randint(1,21)
#while True:
#    print('Take a guess.')
#    guess = int(input())
#    if guess == answer:
#        break
#    elif guess < answer:
#        print('Your guess is too low.')
#    elif guess > answer:
#        print('Your guess is too high.')
    
#print('You got it!')

#Answer must go before the loop, else it is impossible to guess the number,
#since it changes with every iteration.

#To allow only a certain number of guesses:

import random
print('I am thinking of a number between 1 and 20.')
answer = random.randint(1,21)
for guesses in range(6):
    print('Take a guess.')
    guess = int(input())
    
    if guess < answer:
        print('Your guess is too low.')
    elif guess > answer:
        print('Your guess is too high.')
    else:
        break
if guess == answer:
    print(f'You got it! You guessed my number in {str(guesses+1)} guesses.')
else:
    print(f'Nope, my number was {answer}.')

#Did this without looking at the solution and came up with code slightly different from
#sol. suggested in book.    
#Then found out my solution is worse because it did not allow me to continue with two options:
#One when the correct number was guessed before we ran out of guesses and
#the other when we did run out of guesses.
#I broke the loop with an if-statement when the correct answer was given.
#So I fixed it to be more like the solution in the book.
