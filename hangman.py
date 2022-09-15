"""
Simple hangman game
Author: William Lindholm
"""

from eng_dict import *

DICTIONARY_PATH = "dictionary.txt" #path to dictionary

def main():
    dict = eng_dictionary(DICTIONARY_PATH)
    rand_word = dict.getRandomWord()
    rand_word = string_to_list(rand_word)
    greeting()
    #enter gameloop
    gameloop(rand_word)


def gameloop(rand_word):
    guessed_letters = set()
    running = True
    tries_left = 8
    while running and tries_left > 0:
        print("You have: ", tries_left, " more guesses")


        guessed_letter = input("letter: ")
        if guessed_letter in rand_word:
            print(guessed_letter, " Is correct")
            guessed_letters.add(guessed_letter[0])
        elif guessed_letter in guessed_letters:
           print("You have already guessed: ", guessed_letter)
           guessed_letters.add(guessed_letter[0])
        else:
            tries_left -= 1
            guessed_letters.add(guessed_letter[0])

        printProgress(guessed_letters, rand_word)

        #win condition
        if has_won(guessed_letters, rand_word):
            print("Congratulations, you have won")
            return

    print("You lost\nThe correct word was: ")
    printStream = ""
    for letter in rand_word:
        printStream += letter

    print(printStream)




def greeting():
    print("Computer has now generated a random word.\nStart guessing by typing a letter and then pressing enter.\n")

def printProgress(guessed_letters, rand_word):
    printStream = ""
    for i in range(len(rand_word)):
        printStream += " "
        if rand_word[i] not in guessed_letters:
            printStream += "_"
        else:
            printStream += rand_word[i]
    
    print(printStream)


def has_won(guessed_letters, rand_word):
    for letter in rand_word:
        if letter not in guessed_letters:
            return False
    return True


def string_to_list(string):
    string_list = []
    string_list[:0] = string.rstrip()
    return string_list


if __name__ == "__main__":
    main()