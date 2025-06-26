import random

words = ["python", "apple", "laptop", "hangman", "flower"]
word = random.choice(words)
guessed = ['_'] * len(word)
tries = 6
used_letters = []

while tries > 0 and '_' in guessed:
    print("\nCurrent Word:", ' '.join(guessed))
    print("Used Letters:", used_letters)
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("Already guessed.")
        continue
    used_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if '_' not in guessed:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)
