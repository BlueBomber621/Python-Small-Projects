import random
from hangmanaskii import display_hangman
from hangmanwords import words

random_word = words[random.randint(0, len(words) - 1)]
word_label = ""
guesses = []

health = 6

for i in range(1, len(random_word) + 1):
    word_label += "-"

print(f"\nLives left: {health}")
print(display_hangman(health=health))

print(" ".join(word_label.replace("-", "_")) + "\n")

def getGuess():
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or guesses.__contains__(guess):
        while len(guess) != 1 or guesses.__contains__(guess):
            if len(guess) != 1:
                guess = input("Guess a letter (put only one letter): ").lower()
            else:
                guess = input("You already guessed that, guess another: ").lower()

    return guess

while not (word_label == random_word) and health > 0:
    guess = getGuess()
    
    if (random_word.__contains__(guess)):
        for i in range(1, len(random_word) + 1):
            if random_word[i - 1] == guess:
                word_label = word_label[:i - 1] + guess + word_label[i:]
        print(" ".join(word_label.replace("-", "_")) + "\n")
        guesses.append(guess)
    else:
        health -= 1
        print(display_hangman(health=health))
        print(f"Lives left: {health}")
        print(" ".join(word_label.replace("-", "_")) + "\n")
        guesses.append(guess)

if word_label == random_word:
    print("Congragulations! You win!")
elif health < 1:
    print("Too bad, try again next time! The word was: " + random_word)

