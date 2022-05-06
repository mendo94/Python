# using random.randint returns a random number
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, guess again. Too low!!')
        elif guess > random_number:
            print("Sorry, guess again. Too high!!")
        else:
            print(
                f'Yay, congratulations! You have guessed the number {random_number}')


def computer_guess(x):
    # we need to be able to tell the computer if the number is too high or too low
    low = 1
    high = x
    feedback = ""
    # c will equal correcth
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)?)".lower())
        # guesses must be subtracted or added by 1 so the computer knows to go higher or lower
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print(f"Yay, the computer guessed your number {guess}, correctly!")


computer_guess(10)
