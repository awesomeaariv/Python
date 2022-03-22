#High Low Game :)
import random
import time

instructions = input("Welcome to the High Low Game! Would you like the instructions, or are you ready to start?")
if "instructions" in instructions:
    print("I will pick a random number between 1 and 100. Every time you guess a number, I will tell you whether your guess is too high or too low.")

time.sleep(1)
print("Picking a number...")
randomNum = random.randint(1, 100)
time.sleep(5)
currentGuess = int(input("I've picked a number! You can start guessing whenever you're ready."))

while currentGuess != randomNum:
    if currentGuess > randomNum:
        currentGuess = int(input("Too high!"))
    else:
        currentGuess = int(input("Too low!"))

print("Congratulations! Play again soon!")