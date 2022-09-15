"""
Evil hangman game.
Try to get the user to loose by creating "word trees" 
where the game will choose the one revealing the least letters.
"""

DICTIONARY_PATH = "dictionary.txt" #path to dictionary

from eng_dict import *

def main():
    #initialize a new dictionary object
    dict = eng_dictionary(DICTIONARY_PATH)
    
    #generate a random starting word
    starting_word = dict.getRandomWord()
    word_length = len(starting_word)

    #remove any words not matching the starting words length.
    dict.trimDictionaryWordLength(word_length)

    current_progress = wordToTemplate(starting_word)
    
    #greet user
    print("Computer has now generated a random word.\nStart guessing by typing a letter and then pressing enter.\n")
    print(current_progress)

    #enter gameloop
    tries_left = 10
    guessed_letters = set()
    while tries_left > 0:
        #get user input (letter)
        guessed_letter = input("Guess a letter > ")[0]

        #form word familis based on the guessed letter.
        word_families = getWordFamilies(dict.dictionary, guessed_letter)
        
        #filter out and replace current dictionary with the one with the most empty choices.
        biggest_path = max(word_families, key = lambda x: len(set(word_families[x])))
        dict.setDict(word_families[biggest_path])

        #show progress and update variable "currentprogress"
        current_progress = getProgress(biggest_path, current_progress)
        
        #if no word was revealed remove one try
        if guessed_letter not in biggest_path and guessed_letter not in guessed_letters:
            tries_left -= 1
        
        #mark current letter as guessed
        guessed_letters.add(guessed_letter)
        
            
        print("===============================\nProgress: ", current_progress, 
        "\nTries left: ", tries_left, "\n===============================")

        #loose condition
        if tries_left == 0:
            for word in word_families[biggest_path]:
                final_word = word
            print("You have lost!\nThe correct word was: ", final_word)

        #win condition
        if "-" not in current_progress:
            print("Congratulations, you have against all odds won!")
            return


"""
Return a dictionary filled with the different word trees.
Tree will be a list containg words matching the provided template.
The key is the template.
Template will look like: ex. g--d

dict is the current dictionary of words that have not been removed yet.
guessed letter is out most recent guess.
"""
def getWordFamilies(dict, guessed_letter):
    word_families = {}

    for word in dict:
        template = wordToTemplate(word, guessed_letter)
        if template in word_families:
            word_families[template].add(word)
        else:
            word_families[template] = {word}

    """#for debugging
    #for key in word_families:
        #print(key, "\t", word_families[key])"""

    return word_families
    

"""
Convert a word into a template.
if no "focus_letter" aka guessed letter is provided 
the word will be converted into just dashes implying an "empty"
template.
"""
def wordToTemplate(word, focus_letter=None):
    template = ""

    for letter in word:
        if letter == focus_letter:
            template += focus_letter
        else: 
            template += "-"
    
    return template


"""
If the user gets a correct guess add that to the current progress.
for example.
our current guesses has provided us with the progress g--d
the user then guesses o, which for this example is correct.
g--d and -oo- will then be combined to form good.
"""
def getProgress(template, current_progress):
    stringStream = ""

    for i in range(len(template)):
        if template[i] != "-":
            stringStream += template[i]
        else:
            stringStream += current_progress[i]

    return stringStream
    


if __name__ == "__main__":
    main()