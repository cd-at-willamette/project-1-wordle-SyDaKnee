########################################
# Name: Sydney Bell
# Collaborators (if any): I worked alone. 
# GenAI Transcript (if any): I did not use AI, but I used outside sources which will be listed bellow.
# Estimated time spent (hr): 8ish hrs.
# Description of any added extensions: I am not doing any extensions. 
########################################

# https://www.geeksforgeeks.org/python-dictionary/ This is about dictionaries.
# https://www.geeksforgeeks.org/python-string-join-method/ This is about string joining.
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/ This is about f-strings.

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def random_five_letter_word():
    five_lettered_words = [] # Creates an empty list that will collect five-letter words.
    for word in ENGLISH_WORDS: # Goes through every word in the ENGLISH_WORDS file.
        if len(word) == 5: # If the length of the word is five letters, ->
            five_lettered_words.append(word) # add the word to the end of the "five_lettered_words" list.
    return random.choice(five_lettered_words).upper() # Once you have collected all the five-letter words from ENGLISH_WORDS, randomly choose one word and return it in uppercase.

def wordle():
    # The main function to play the Wordle game.
    answer_str = random_five_letter_word() # Chooses a random five letter word as the secret word to guess during the game.


    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        
        current_row = gw.get_current_row() # Gets the current row number where the guess was entered.
        guess = word_from_row(current_row) # Gets the word from the row where the guess was entered.
        guess_low = guess.lower() # Converts the guess to lowercase (as formatted in ENGLISH_WORDS).

        if is_english_word(guess_low): # Checks is the guessed word is valid in the ENGLISH_WORDS collection.
            color_row(current_row, guess, answer_str) # If the word is valid, the function should be called to color the row to display which letters in the guess were correct. 
            if guess == answer_str: # If the guess is the same as the answer, ->
                gw.show_message("You guessed it!") # Display a message on the screen that shows it is correct.
                gw.set_current_row(N_ROWS) # Stop the game.
            else:
                if current_row + 1 < N_ROWS: # If the guess is incorrect, move to the next row to guess again, -> 
                    gw.set_current_row(current_row + 1) # move to the next row to guess again.
                else:
                    gw.show_message(f"You lost, the asnwer is {answer_str}.") # Unless if the next row is the last row: then display a message that states the game has been lost.
        else:
            gw.show_message("Try again. Word not in list.") # If the word is not valid, display a message that says to try a different guess.
 

    def word_from_row(row):
        letters = [] # An empty list to store letters in.
        for col in range(5): # Loops through the five columns/letters.
            letter = gw.get_square_letter(row, col) # Gets the letter from the current row and column.
            letters.append(letter) # Adds the letter to the end of the "letters" list.
        return ''.join(letters) # After it collects all the letters in each row, it joins/combines them and returns the word.
    

    def color_row(row:int, guess:str, answer:str):

        correct = [False] * 5 # Creates a list that tracks if each letter in the guess is in the correct position. Starts at five "False" values, but subject to change when the letters are checked.
        present = [False] * 5 # Creates a list that tracks if a letter is present but in the wrong position.

        letter_count = {} # An empty dictionary that counts how many times a letter appears in the answer.
        for letter in answer: # Loops through each letter in the answer.
            letter_count[letter] = letter_count.get(letter, 0) + 1 # Adds the letter to the dictionary count or increases it if it is already there.

        for col in range(5): # Loops through each letter in the guess.
            if guess[col] == answer[col]: # If the letter positioning for the guess matches the letter positioning for the answer, ->
                gw.set_square_color(row, col, CORRECT_COLOR) # set the color of the square to green,
                gw.set_key_color(guess[col], CORRECT_COLOR) # and set the color of the keyboard tile to green.
                correct[col] = True # When it is found that a letter in the guess is in the correct postiion, mark that letter as correct in the current column.
                letter_count[guess[col]] -= 1 # Decreases the count of that specific letter in the dictionary to keep track of how many times each letter from the answer can still be matched to a "present" or "correct" value.

        for col in range(5): # Loops through each letter in the guess.
            if not correct[col]: # If the letter is not marked as "correct", ->
                if guess[col] in letter_count and letter_count[guess[col]] > 0: # and if the letter is in the dictionary and there are still remaining instances of this letter available in the answer, ->
                    gw.set_square_color(row, col, PRESENT_COLOR) # set the color of the square to yellow,
                    gw.set_key_color(guess[col], PRESENT_COLOR) # and set the color of the keyboard tile to yellow.
                    letter_count[guess[col]] -= 1 # Then decrease the count of that specific letter in the dictionary by one.
                else:
                    gw.set_square_color(row, col, MISSING_COLOR) # Otherwise, set the color of the square to grey,
                    gw.set_key_color(guess[col], MISSING_COLOR) # and set the color of the keyboard tile to grey.


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
