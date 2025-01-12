import random
from words_hangman import hangman_draw
from words_hangman import words

# function to allow the user to input a file name and read a list of words from the file
def file_select():
    print("Please write a txt file name (must have 1 word per line without being in a list)")
    while True:
        try:
            user_file = input("Enter your file name with the extension: ")
            with open(f"{user_file}.txt", 'r') as file:  # 'r' = reading the file
                word_list = [line.strip() for line in file.readlines()]  # get all the lines on the other file
            return word_list  # return the lines
        except FileNotFoundError:
            pass

# function to allow the user to select a word, either from a predefined list or their own file
def word_select():
    print("Welcome to the Hangman game!!")
    print("Hope you'll have a great time!!")
    print("\n1. For playing with an existing list")
    print("2. For playing with your own list")
    user_num = int(input("Enter a number: "))
    
    while user_num != 1 and user_num != 2:
        user_num = int(input("Enter a valid number: "))
    
    match user_num:
        case 1:
            print("----------------------------")
            print("\nTheme: Foods")
            return random.choice(words)  # select one word from a predefined list
        case 2:
            print("\nTheme: Your own choice")
            select = file_select()  # call the lines on the other file
            return random.choice(select)  # randomly select one line

# function to display the current state of the word with guessed and blank spaces
def display(word, guess):
    prompt = ""
    # iterate through each character in random word
    for letter in word:
        if letter in guess:
            prompt += letter  # if letter chosen is in the random word
        else:
            prompt += "_"  # if letter chosen is not in the random word
    return prompt

# main game logic
def main():
    guess = []  # storing chosen letters
    choice_word = word_select()
    attempts = len(choice_word) + 3  # number of attempts of the user
    correct_attempts = 0
    wrong_attempts = 0
 
    # User menu
    print("\n1. Play the game")
    print("0. close the program")

    while True:
        try:
            ch = int(input("Please choose a number: "))
            if ch == 1 or ch == 0:
                break
            else:
                print("You did not pick 0 or 1")
                pass
        except ValueError:
            print("You did not pick a number. Try again.")
            pass

    match ch:
        case 1:
            current = None
            while attempts > 0:
                print("\n--------------------------------")
                # displaying the current state of the game
                print("Attempts left:", attempts)
                current = display(choice_word, guess)
                print("Word:", current)
                user_letter = input("Choose a letter: ").lower()

                # checking user input and updating game state
                if user_letter in guess:
                    print("You have already used this letter. Try another")
                elif len(user_letter) > 1:
                    print("You entered too many letters")
                elif len(user_letter) < 1 or user_letter.isalpha() is False:
                    print("You entered a number or no letters")
                elif user_letter.isalpha() and user_letter not in choice_word:
                    attempts -= 1
                    wrong_attempts += 1
                    print("This word does not contain this letter")
                else:
                    correct_attempts += 1

                # displaying the hangman drawings based on wrong attempts
                if wrong_attempts == 0:
                    print(hangman_draw[0])
                elif wrong_attempts == 1:
                    print(hangman_draw[1])
                elif wrong_attempts == 2:
                    print(hangman_draw[2])
                elif wrong_attempts == 3:
                    print(hangman_draw[3])
                elif wrong_attempts == 4:
                    print(hangman_draw[4])
                elif wrong_attempts == 5:
                    print(hangman_draw[5])
                elif 6 <= wrong_attempts < len(choice_word) + 5:
                    print(hangman_draw[6])

                # add the letter chosen by the user to a list
                guess.append(user_letter)

                # checking if every element of the random word is in the list of correct guessed letters
                if set(choice_word) <= set(guess):
                    # display winning message
                    print("The stickman did not die! Congratulations!")
                    print("Your word was:", choice_word)
                    print("\nStatistics:", "\nCorrect attempts:", correct_attempts)
                    print("Wrong attempts:", wrong_attempts)
                    if wrong_attempts == 0:
                        print("Congrats! Perfect game!")
                    print("Guesses taken:", wrong_attempts + correct_attempts)
                    print("Attempts left:", attempts)
                    # calculate percentage of correct guesses
                    percentage = (correct_attempts / (correct_attempts + wrong_attempts)) * 100
                    print(f"Percentage of correct guesses: {percentage:.2f}%")
                    break

            # check if there are no attempts left
            if attempts == 0:
                print(hangman_draw[7])
                print("You let the stickman die! Poor man! Did not deserve this :(")
                print("The word was:", choice_word)
                print("\nStatistics:", "\nCorrect attempts:", correct_attempts)
                print("Wrong attempts:", wrong_attempts)
                print("Guesses taken:", wrong_attempts + correct_attempts)
                # calculate percentage of correct guesses
                percentage = (correct_attempts / (correct_attempts + wrong_attempts)) * 100
                print(f"Percentage of correct guesses: {percentage:.2f}%")
                print("Your current word:", current)
        case 0: 
            # close the program
            x = 0
        case _:
            # close the program
            print("The Number is not among these!")
            pass

# execute the main function to start the game
if __name__ == "__main__":  # checks if the script is being run as the main program
    main()
