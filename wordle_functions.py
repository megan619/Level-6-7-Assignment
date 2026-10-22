# Selects and returns a secret word.

from random import choice

def choose_word():
    words = [
        "grape", "lemon", "mango", "peach", "hairy"
        "chair", "table", "plant", "house", "brick",
        "cloud", "storm", "light", "flame", "stone",
        "piano", "music", "dance", "laugh", "smile",
        "beach", "ocean", "river", "shark", "whale",
        "tiger", "horse", "zebra", "eagle", "mouse"
    ]
    return choice(words)


# Gets and validates the players guess.
def get_guess(previous_guesses):
    while True:
        guess = input("Enter your guess (5 letters): ").lower()

        if len(guess) != 5 or not guess.isalpha():
            print("Invalid input. Please enter a 5-letter word.")

        elif guess in previous_guesses:
            print("You already guessed that word. Try again!")

        else:
            return guess



# Compares the guess with the secret word and returns feedback.
def evaluate_guess(guess,secret_word):
        feedback = []
        for i in range(5):
            if guess[i] == secret_word[i]:
                feedback.append("G")  # Correct letter and position
            elif guess[i] in secret_word:
                feedback.append("Y")  # Correct letter, wrong position
            else:
                feedback.append("-")  # Incorrect letter
        return guess, feedback



# Displays the guess and its feedback.
def display_guess(guess, feedback):
    print(f"Your guess: {guess}")
    print(f"Feedback: {' '.join(feedback)}")


# Determines whether the player has guessed the word.
def has_won(guess, secret_word):
    return guess == secret_word




