import random

number = random.randint(1, 100) # Variable to create a random integer from 1-100
attempts = 0 # Variable to track attempts
guess = int(input('Enter your guess:')) # Variable for user to input a number

while number != guess: # Checks if the random integer and guess is not equal

    attempts += 1
    if number > guess:
        print('Too low')
    else:
        print('Too high')
    
    guess = int(input('Try again:'))

    if attempts >= 6:
        print(f'Game over. The number was {number}.')
        break

if attempts < 6:
    attempts += 1
    print(f'You took {attempts} attempts to find the number')
