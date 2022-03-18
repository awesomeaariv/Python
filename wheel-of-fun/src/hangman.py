# Hangman Project v1.0.3

import random #importing random to generate random number
words = ["cat", "dog", "sheep", "abomination", "destruction", "immobilization", "excitement", "troll"] #word array

print("Welcome to Hangman!")
#### Checks if user is ready to start ####
ready = input("Are you ready to start? Y/N")
if ready == "N" or ready == "No" or ready == "n" or ready == "no":
    print("That's okay, see you next time!")
    quit()

incorrectGuesses = 0 #setting up variable for number of wrong guesses
word = random.choice(words) #random word from array
currentGuess = "_ " * len(word) #setting up word w/ blanks, ex. cat = _ _ _
lettersGuessed = [] #setting up dictionary of letters the user guessed

print("All right! Let's begin!")
print("Your word has {} letters, and you have 6 wrong guesses before the game is over.".format(len(word)))
print("Every time you type a letter, I will tell you where in the word it is located, if in the word at all. You may start whenever you want.")

while incorrectGuesses < 6: #checks if game should be over
    letter = input()
    if letter == "what letters have I guessed?": #user asks for list of guessed letters
        print("The letters you have guessed are:\n" + str(lettersGuessed))
        continue

    if "the word is" in letter: #checks if user is guessing the whole word
        if word in letter:
            print("Wow, that was impressive! You guessed the word correctly. Play again soon!")
        else:
            incorrectGuesses += 1
            print("Sorry, that wasn't the word. You have {} wrong guesses left. Try again.".format(6 - incorrectGuesses))

    if not letter.isalpha() or len(letter) != 1: #checks if user's response is a letter
        letter = input("Guess a letter, please.")
        while not letter.isalpha() or len(letter) != 1:
            letter = input()

    if letter in lettersGuessed: #checks if user already guessed this word
        letter = input("You've already guessed this letter. You can type 'what letters have I guessed?' to see a list of guessed letters. Please try another one.")
        while letter in lettersGuessed:
            letter = input()

    lettersGuessed.append(letter) #adds letter to the lettersGuessed dictionary
    index = 0
    indexes = []
    for i in word: #iterates through each character in the word
        if i.upper() == letter.upper(): #checking if the letter matches
            indexes.append(index)
        index += 2 #adds 2 to the index to count for the space after the underscores
    for i in indexes: #iterates through the indexes; is ignored if indexes is empty (letter doesn't match the word)
        currentGuess = currentGuess[:i] + letter.lower() + currentGuess[i+1:] #replacing a certain underscore with the letter
    print(currentGuess)
    if len(indexes) > 0: #if the letter matched
        if "_" not in currentGuess: # if user won
            print("Congrats! It's pretty clear that you're an ace at the game. Play again soon!")
            quit()
        print("Good job! {} was in the word. Go ahead and try another letter!".format(letter))
    else:
        incorrectGuesses += 1 
        print("Sorry, {} was not in the word. You have {} wrong guesses left. Please try another letter.".format(letter, 6 - incorrectGuesses))

print("Oh no! It looks like you're out of guesses. The word was {}. Try again soon!".format(word.lower())) #if user lost