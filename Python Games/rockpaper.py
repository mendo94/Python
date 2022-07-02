import random

# use a function that the user can enter an input to play against the computer


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper', 's' for scissors? ")
    # allow the computer to randomly choose rock, paper or scissors
    computer = random.choice(['r', 'p', 's'])
    print(f"The conmputer chose {computer}")
    # establish a rule for when there is a tie
    if user == computer:
        return 'It is a tie!'

    if is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'

    # define a condition that determines who wins


def is_win(player, opponent):
    # conditions that return true if the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
# print(f"You chose {user} and the computer chose {computer}")
