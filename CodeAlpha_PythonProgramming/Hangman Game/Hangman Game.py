import random

words = ["python", "coding", "laptop", "gaming", "future"]
word = random.choice(words)

hidden_word = ["_"] * len(word)
tries = 6
used_letters = []

print("Welcome to Hangman Game")

while tries > 0 and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    print("Used Letters:", used_letters)
    print("Remaining Tries:", tries)

    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already used this letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        print("Correct Guess!")
    else:
        tries -= 1
        print("Wrong Guess!")

if "_" not in hidden_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
