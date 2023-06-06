# Python Hangman (DSA PROJECT)
A hangman game in Python is a text-based guessing game where players attempt to guess a secret word by suggesting letters one at a time. The game starts by selecting a random word from a predefined list, which remains hidden from the player. The player's objective is to guess the word correctly before running out of attempts. Each incorrect guess results in a penalty, where a part of the hangman's gallows and stick figure is drawn. The game continues until the player successfully guesses the word or the hangman is fully drawn, leading to the player's loss.

Evil Hangman is a variant of the classic Hangman game that adds an extra layer of challenge and frustration for players. In this version, instead of selecting a single word at the beginning of the game and sticking with it, the computer dynamically changes the target word based on the player's guesses.

<sub>sample output:</sub>
```
Guess a letter > l
===============================
Progress:  ------ 
Tries left:  9 
===============================
Guess a letter > r
===============================
Progress:  ------ 
Tries left:  8 
===============================
Guess a letter > e
===============================
Progress:  ------ 
Tries left:  7 
===============================
Guess a letter > g
===============================
Progress:  ------ 
Tries left:  6 
===============================
Guess a letter > y
===============================
Progress:  ------ 
Tries left:  5 
===============================
Guess a letter > p
===============================
Progress:  ------ 
Tries left:  4 
===============================
Guess a letter > v
===============================
Progress:  ------ 
Tries left:  3 
===============================
Guess a letter > c
===============================
Progress:  ------ 
Tries left:  2 
===============================
Guess a letter > t
===============================
Progress:  ------ 
Tries left:  1
===============================
Guess a letter > o
===============================
Progress:  ------
Tries left:  0
===============================
You have lost!
The correct word was:  maddis
```

As you can see, this version is very hard, below you can see how a normal version of hangman would play out:

```
Start guessing by typing a letter and then pressing enter.

You have:  8  more guesses
letter: d
d  Is correct
 _ _ _ _ _ d _ _ _ _
You have:  8  more guesses
letter: p
 _ _ _ _ _ d _ _ _ _
You have:  7  more guesses
letter: s
 _ _ _ _ _ d _ _ _ _
You have:  6  more guesses
letter: r
 _ _ _ _ _ d _ _ _ _
You have:  5  more guesses
letter: n
n  Is correct
 _ _ _ _ n d _ _ _ _
You have:  5  more guesses
letter: m
 _ _ _ _ n d _ _ _ _
You have:  4  more guesses
letter: t
 _ _ _ _ n d _ _ _ _
You have:  3  more guesses
letter: w
 _ _ _ _ n d _ _ _ _
You have:  2  more guesses
letter: p
You have already guessed:  p
 _ _ _ _ n d _ _ _ _
You have:  2  more guesses
letter: o
o  Is correct
 o _ _ _ n d _ _ _ _
You have:  2  more guesses
letter: l
l  Is correct
 o _ _ _ n d _ _ l _
You have:  2  more guesses
letter: a
a  Is correct
 o _ _ _ n d a _ l _
You have:  2  more guesses
letter: r
You have already guessed:  r
 o _ _ _ n d a _ l _
You have:  2  more guesses
letter: y
 o _ _ _ n d a _ l _
You have:  1  more guesses
letter: g
 o _ _ _ n d a _ l _
You lost
The correct word was:
offendable
```