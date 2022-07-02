import random
# link the file of random words from word.py

from words import words
from hangman_visual import lives_visual_dict
import string

# the word file has a bunch of invalid words (words with spaces in them) so we must make a function that picks a valid word for hangman


def get_valid_word(words):
    # random.choice takes in a list and randomly chooses something from that list
    word = random.choice(words)
    # create a while loop that will keep searching words without spaces or dashes
    while '-' in word or ' ' in word:
        word = random.choice(words)
    # return the word and add .upper so the letters are uppercase
    return word.upper()


def hangman():
    word = get_valid_word(words)
    # the next variable will keep track of the letters in the word
    word_letters = set(word)
    # create an alphabet variable using .ascii built in function
    alphabet = set(string.ascii_uppercase)
    print("this is the alphabet", alphabet)
    # the next variable will keep track of the letters already guessed
    used_letters = set()

    lives = 7
    # create a while loop that will keep asking for letters until the word is guessed
    while len(word_letters) > 0 and lives > 0:
        # ' '.join turns the list into a string separated by a space.
        print("You have", lives, "lives left and you have used these letters: ",
              ' '.join(used_letters))

        # making the current word
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        # getting user input
        user_letter = input("Guess a letter: ").upper()
        # if letter is a valid letter that has not been used yet, then add letter to used letter set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # if the letter that was guessed is in the hangman word, then remove that letter from word_letters
            if used_letters in used_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                # take away one life
                lives = lives - 1
                print("Letter is not in the word")
        elif user_letter in used_letters:
            print("You already guessed that letter!!!")
        else:
            print("Invalid character. Try again.")

        # loops here when length of word_letters == 0 or when lives == 0
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")


if __name__ == '__main__':
    hangman()
