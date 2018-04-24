import string

from util.puzzle_runner import Puzzle, run_puzzles


# --------------------------------------------------------------------------------
# OVERVIEW
# -----------
#
# All the puzzles are solved by finding a single word in the list of words
# (called 'word_list') that is passed into each puzzle function.
#
# The general idea is to search through the words in the list using a loop
# rather than trying to figure it out by hand because it would take way too long!
#
# If you can't figure out a puzzle, skip to the next one and ask if you get really stuck!
#
# Scroll down for the functions for the six puzzles.
# --------------------------------------------------------------------------------


# This function will come in handy for Puzzle Six
def calculate_letter_scrabble_value(letter):
    value = 0
    one_point = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r']
    two_point = ['d', 'g']
    three_point = ['b', 'c', 'm', 'p']
    four_point = ['f', 'h', 'v', 'w', 'y']
    five_point = ['k']
    eight_point = ['j', 'x']
    ten_point = ['q', 'z']
    if letter in one_point:
        value = 1
    elif letter in two_point:
        value = 2
    elif letter in three_point:
        value = 3
    elif letter in four_point:
        value = 4
    elif letter in five_point:
        value = 5
    elif letter in eight_point:
        value = 8
    elif letter in ten_point:
        value = 10

    return value


# ---------------------------------------------------------------------------------------------------
# PUZZLE 1
# ---------
#
# Find a word in the word list that starts with the letter 'e' and contains the word 'cat'.
#
# Hints:
# - Use a for loop to check all the words in the list one by one. (e.g. for word in word_list:)
# - You can index into letters of a word like so: word[1] = 2nd Letter of a word.
# - You can use the 'in' keyword to see if a string is part of another string (e.g. if 'dog' in word:)
# ---------------------------------------------------------------------------------------------------
def puzzle_one(word_list):
    task = "Find a word in the list that starts with the letter 'e' and contains the word 'cat'."
    answer = "DEFAULT ANSWER"
    
    # add code to find the correct answer here, and assign it to the variable 'answer'

    return Puzzle(task, answer)


# ---------------------------------------------------------------------------------------------------
# PUZZLE 2
# ----------
#
# Find an eleven letter word, where the first and last letter are the same
#
# Hints:
# - Remember that len(thing) finds the length of a thing.
# - Use word[0] to find the first letter of a word, and word[-1] to find the last.
# ----------------------------------------------------------------------------------------------------
def puzzle_two(word_list):
    task = "Find an 11 letter word where the first and last letter are the same"
    answer = "DEFAULT ANSWER"

    # add code to find the correct answer here, and assign it to the variable 'answer'

    return Puzzle(task, answer)


# ---------------------------------------------------------------------------------------------------
# PUZZLE 3
# ----------
#
# Find a word beginning with the letter 'b' that is a palindrome.
#
# Hints:
# - A palindrome is a word that is the same read forward as backward e.g. LEVEL. 
#   This means the first letter equals the last, the second letter equals the second last and so on.
# - You can index into a word backwards using negative numbers e.g. word[-1] == the last letter of the word.
# - Try using a for loop with a range(0, len(word)) statement to get an index for each letter of our word
#   then use it to get the first letter and the last letter of our word. Then, when it increases, gets the
#   2nd and 2nd to last letter of our word. Remember the last letter is at -1 and the first is 0.
# ---------------------------------------------------------------------------------------------------
def puzzle_three(word_list):
    task = "Find a word beginning with the letter 'b' that is a palindrome."
    answer = "DEFAULT ANSWER"
    
    # add code to find the correct answer here, and assign it to the variable 'answer'

    return Puzzle(task, answer)


# ---------------------------------------------------------------------------------------------------
# PUZZLE 4
# ----------
#
# Find a 3 letter word that contains no vowels and that begins with the letter 's'.
#
# Hints:
# - You can use 'and' to check multiple conditions in one if statement (e.g. if x and y and z:)
# ----------------------------------------------------------------------------------------------------
def puzzle_four(word_list):
    task = "Find a 3 letter word, containing no vowels and that begins with the letter 's'."
    answer = "DEFAULT ANSWER"
    vowels = ['a', 'e', 'i', 'o', 'u']

    # add code to find the correct answer here, and assign it to the variable 'answer'

    return Puzzle(task, answer)


# ---------------------------------------------------------------------------------------------------
# PUZZLE 5
# ----------
#
# Find a word that is 3 letters long AND contains no letters in the nonsense phrase 'jeff's trained wax bicycles'.
#
# Hints:
# - You can use the special all() function to test a condition on all letters in a word. e.g:
#
#       if all( letter == 'a' for letter in word)
#
#   would be true if all letters in the word were 'a'.
# - You can also use the 'in' keyword to see if a letter is part of a word or a list of letters.
#   (e.g. if letter in word: )
# ---------------------------------------------------------------------------------------------------
def puzzle_five(word_list):
    task = "Find a word that is 3 letters long AND contains no" \
           " letters in the nonsense phrase 'jeff's trained wax bicycles'."
    answer = "DEFAULT ANSWER"
    jeffs_trained_wax_bicycles = "jeff's trained wax bicycles"

    # add code to find the correct answer here, and assign it to the variable 'answer'

    return Puzzle(task, answer)


# ---------------------------------------------------------------------------------------------------
# PUZZLE 6
# ----------
#
# Find a word with a normal scrabble value of 24.
#
# Hints:
# - Use the calculate_letter_scrabble_value(letter) function defined at the top of this file.
# - A word's scrabble value is just the sum of all of its letter's scrabble values.
# ----------------------------------------------------------------------------------------------------
def puzzle_six(word_list):
    task = "Find a word with a normal scrabble value of 24"
    answer = "DEFAULT ANSWER"

    # add code to find the correct answer here, and assign it to the variable 'answer'

    return Puzzle(task, answer)


words = []
with open("util/word_list.txt", "r") as wordsFile:
    for line in wordsFile:
        exclude = set(string.punctuation)
        word_string = line.lower().rstrip()
        word_string = ''.join(ch for ch in word_string if ch not in exclude)
        if len(word_string) > 0:
            words.append(word_string)
            
run_puzzles(puzzle_one(words), puzzle_two(words), puzzle_three(words),
            puzzle_four(words), puzzle_five(words), puzzle_six(words))
