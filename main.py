from wordle_functions import get_guess, evaluate_guess, choose_word, display_guess, has_won

#play again loop starts here
play_again = "y"
while play_again == "y":

#welcome player to the game
    print("Welcome to Wordle!")

#choose random word
    secret_word = choose_word()

#initialize number of attempts and previous guesses
    previous_guesses = []
    attempts = 0
    while attempts < 6:
        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)
        guess, feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        #keep track of the number of attempts
        attempts += 1 

        #if the player has won, congratulate them and break the loop.
        if has_won(guess, secret_word):
            print("Congratulations! You've guessed the word!")
            break

        #if the player has not won, inform them of the number of attempts left and give feedback.
        else:
            if attempts < 6:
                print(f"You have {6 - attempts} attempt(s) left.")
    #if the player runs out of attempts and has not guessed the word, inform them of the secret word.
    if attempts == 6 and not has_won(guess, secret_word):
        print(f"Sorry! The secret word was {secret_word}.")

    #ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye!")


        