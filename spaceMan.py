import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    ans = "".join(letters_guessed)
    if secret_word == ans:
        return True
    return False

def get_guessed_word(letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    temp = "".join(letters_guessed)
    return temp

def is_guess_in_word(guess, secret_word, letters_guessed, wrong):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    correct = False
    length = len(secret_word)
    for index in range(length):
        if guess == secret_word[index]:
            letters_guessed[index] = guess
            correct = True
    if not correct:
        wrong.append(guess)
    return correct

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = list()
    life = len(secret_word) 
    for fill in range(len(secret_word)):
        letters_guessed.append("_ ")
    
    wrong = list()
    #TODO: show the player information about the game according to the project spec
    print("welcome to Spaceman, the goal of this game is to guess a mystery word character by character")
    print(f"""wrong guess will make you lose a life ({life} live(s) total), \nand correct guesses will show their positions in the word""")
    print(get_guessed_word(letters_guessed))
    while life > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        invalid = True
        while invalid:
            guess = input("Please enter a letter: ")
            if guess.isalpha() and len(guess) == 1:
                guess = guess.lower()
                invalid = False
                if guess in wrong or guess in letters_guessed:
                    print("youve guessed this already")
                    invalid = True
            else:
                print("not a valid guess")
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word, letters_guessed, wrong):
            print("Correct Guess")
        else:
            life -= 1
            print("incorrect guess")

        #TODO: show the guessed word so far
        print(get_guessed_word(letters_guessed))
        print("Wrong guesses: ")
        print("".join(wrong))
    #TODO: check if the game has been won or lost
    if(life == 0):
        print("You've lost the game")
        print("The correct word was: " + secret_word)
    elif is_word_guessed(secret_word, letters_guessed):
        print("You've won the game")


#These function calls that will start the game
    
if __name__ == '__main__':
    again = True
    while again:
        secret_word = load_word()
        spaceman(secret_word)
        confirm = input("play again? (y/n): ")
        yes_no = True
        while yes_no:
            if confirm == "n":
                again = False
                yes_no = False
            elif confirm == "y":
                yes_no = False
            else:
                print("Invalid choice")


def test_is_guess_in_word():
   assert is_guess_in_word('a', 'apple', ['_ ', '_ ', '_ ', '_ ', '_ '], [])    #test correct guess
   assert not is_guess_in_word('b', 'apple', ['_ ', '_ ', '_ ', '_ ', '_ '], [])    #test bad guess 

def test_get_guessed_word():
    assert get_guessed_word(['a', 'p', 'p', '_ ', '_ ']) == "app_ _ "

def test_is_word_guessed():
    assert not is_word_guessed("apple", ['a', 'p', 'p', '_ ', '_ '])    #test not guessed
    assert is_word_guessed("apple", ['a', 'p', 'p', 'l', 'e'])      #test guessed