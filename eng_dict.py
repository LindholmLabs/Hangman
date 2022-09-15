"""
Help file for hangman program.
Read a dictionary then provide functions to get a random word.
"""

import random


class eng_dictionary():
    """
    Constructor function.
    Read all lines in a dictionary text file and store in dictonary.
    """
    def __init__(self, dictionary_path) -> None:
        self.dictionary = set(line.strip().lower() for line in open(dictionary_path, 'r'))


    """
    Return entire dictionary
    """
    def getDictionary(self):
        return self.dictionary


    """
    Return word from dictionary at specified position
    """
    def getWordAt(self, pos):
        return self.dictionary[pos]


    """
    Return one random word from the english dictionary
    """
    def getRandomWord(self):
        numberOfWords = len(self.dictionary)
        rand = random.randint(0, numberOfWords)
        
        count = 0
        for word in self.dictionary:
            count += 1
            if count == rand:
                return word


    """
    Get all the possible words for example:
    -O-- would return A set containing {"good", "goal", "goon"} etc
    VAR: template = ex. "--u---" or d--g
    """
    def getPossibleWords(self, template):
        word_length = len(template)
        output = set()

        for word in self.dictionary:
            if self.__wordMatchesTemplate(template, word):
                output.add(word)
        
        return output


    """
    Removes all words in the dictionary
    that are not of the specified length.
    """
    def trimDictionaryWordLength(self, length):
        new_dict = set()

        for word in self.dictionary:
            if len(word) == length:
                new_dict.add(word)

        self.dictionary = new_dict


    """
    Help function for getPossibleWords()
    that returns if a given word matches the template
    returns true of false.
    """
    def __wordMatchesTemplate(self, template, word):
        for i in range(len(template)):
            if template[i] != "-":
                if template[i] != word[i]:
                    return False
        
        return True


    """
    Manually set the dict to a new set
    """
    def setDict(self, new_dict):
        self.dictionary = new_dict
