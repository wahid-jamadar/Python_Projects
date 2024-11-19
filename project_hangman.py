import random

def hangman():
    # List of words to choose from
    word_list = ['python', 'development', 'hangman', 'programming', 'Dumbosaurus', 'Wahid', 'internship']
    
    word = random.choice(word_list)
    word_length = len(word)
    guessed_word = ['_'] * word_length  # Create a list of underscores as placeholders for the word
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Number of allowed incorrect guesses
    
    print("Welcome to Hangman!")
    print(" ")
    print("Guess the word, one letter at a time.")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")
    
    while incorrect_guesses < max_incorrect_guesses and ''.join(guessed_word) != word:
        print("\nWord: ", ' '.join(guessed_word))  # Show the current state of the word
        print("Guessed letters:", ' '.join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            # Reveal the guessed letter in the word
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

    # Check if the player has won or lost
    if ''.join(guessed_word) == word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nSorry, you've run out of guesses. The word was:", word)

# Start the game
hangman()