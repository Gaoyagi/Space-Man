#readme
#George Aoyagi CS1.1 section B
#plays a game of spaceman
#goal is to guess a mystery word, letter by letter, wrong guesses reduce life
#the game ends when you are out of lives or you guess the word
#you have as many lives as there are letters in the words
#after the game is over you have an option to play again

#######################Pseduo code#########################################
letters_guessed: a list that holds the correctly guessed letters and _ for unguessed letters
secret_word: a string variable that holds the randomized word from the word
guess: the suer inputted guess for that round
wrong: list that holds all the incorrect guesses the user inputs

#checks if the user has guessed all the letters in the answer yet
is_word_guessed(secret_word, letters_guessed):
    converts secret_word string into a list called ans
    then checks is letters_guessed is the same list as the Ans
    if they are equal:
        then the word has been guessed and should return True
    if they aren't equal:
        then the word hasn't been guessed and should return false

#prints out all the currently guessed letters
get_guessed_word(letters_guessed):
    creates an empty string
    loop through all of letters_guessed
        add each element from letters_guessed to the empty string
    prints the string of letters_guessed

#checks if the user letter guess is in the answer
is_guess_in_word(guess, secret_word, letters_guessed, wrong):
    creates a boolean variable correct, sets is to False
    loop through the length of the secret_word
        if the guess is equal to the element at the index of secret_word
            then change the element of letters_guessed at that same index
            make correct True
    if correct is true, return True
    else (correct is false)
        add the guess to the wrong guess list
        return False

#runs one game of Spaceman
spaceman(secret_word):
    number of lives set to the length of secret_word
    creates empty list for correct guesses
    loop though length of secret_word:
        fills correct guesses with _
    creates empty list for wrong guesses
    prints out instructions for game
    prints out all current correct guesses
    loop the game as long as life isn't 0 and all the letters of the word hasn't been guessed
        create boolean invalid and set to true
        loop while invalid is letters_guessed
            ask user for a guess
            check if the guess is only 1 alphabetical character
                then convert the guess into a lower case letters
                change invalid to False
                check if the guess has been guessed before
                    if it has print that it has
                    change invalid back to True
            if its not a single letter
                    then tell user its an invalid guess
        now check if the guess is in the mystery word
            if it is tell the user is correct
            else subtract life by 1 and tell user the guess is Wrong
            print all the current correct guesses
            print all the wrong guesses the player has had so far
    if the life value is 0
        tell the suer he lost the game and print what then answer was
    if the letters_guessed has all the letters
        tell user they won

create global bool again and set it to True
loop the following while again is True
    create the secret_word answer and give it a random word from file
    run the game with secret_word as the argument
    ask the user if they want to play again
    create bool variable true_false and set it to true
        loop while true_false is true
            check to see if the user input is a either y or n
                if the user inputs an n
                    change again and true_false is False
                if the user inputs a y
                    change true_false to False
                if neither of those
                    then tell the user thats an improper input
