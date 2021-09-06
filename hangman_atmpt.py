correct_word = input("What is the word?") # Allow someone to choose the word for someone else to guess
unique_length = set(correct_word) # Determine number of unique characters in word
guesses = int(input("How many guesses?")) # Prompt for number of guesses allowed
while guesses < len(unique): # While the inputted number of guesses is invalid (not enough for the player to possibly win)
    print("Not enough guesses to guess this word.") # Print message about issue
    guesses = int(input("How many guesses?")) # Reprompt for number of guesses (until valid number is given)
length = len(correct_word)
guessed_word = "_" * length # Initialize string showing which correct letters have been guessed and which have not
while guessed != correct_word and guesses != 0: # While the full word has not yet been guessed, and there are still guesses left
    letter_guess = input("Guess a letter: ")
    guessed_letters = []
    if letter_guess in guessed_letters: # If inputted letter has already previously been guessed
        print("You already guessed this.")
        continue
    for i in range(length):
        if letter_guess == correct_word[i]:
            guessed_word = guessed_word[0:i] + correct_word[i] + guessed_word[i+1:length] # Update guessed_word with letters filled in if guessed
    print(guessed_word) # Show player updated guessed_word
    guesses -= 1 # Decrement guesses since a guess has been used
if guessed_word == correct_word: # If player was able to guess all letters
    print("You won!") # Display winner message
else:
    print("You lost!") # Display loser message
