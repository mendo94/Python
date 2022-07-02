# using random.randint returns a random number
import random

# to get started we need a function to pass in arguments
# put x in the parameter of guess so we can pass that into the random get number function


def guess(x):
    random_number = random.randint(1, x)

    # set guess equal to zero so that the random number can never be zero
    guess = 0
    # create a while loop to guess a number if it does not equal the computer's number

    while guess != random_number:

        # once the computer generates a number, we must guess and the computer will tell us if we need to guess higher or lower
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, guess again. Too low!!')
        elif guess > random_number:
            print("Sorry, guess again. Too high!!")
        else:
            print(
                f'Yay, congratulations! You have guessed the number {random_number}')


# allow 10 random numbers
guess(10)
