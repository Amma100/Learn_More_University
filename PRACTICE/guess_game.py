from check_module import *

# using loops to check a value or letter in a word
print("\n\t\t\t\t\t\t\t ------------------------------\n\t\t\t\t\t\t\t|    WELCOME TO HANGMAN GAME   |\n\t\t\t\t\t\t\t------------------------------\n")
print("-------------------------------------------\n|\t=============================       |\n|\tEnter'1' to play game             |\n|\tEnter'2' to view instruction        |\n|\tEnter'3' to quit                    |\n|\t=============================       |\n -------------------------------------------")
print("\n\n")
player_name = input("Enter player name: ").upper()

while True:
    # get user response for option above
    entry_1 = int(input("\nEnter a value from the listed option above: "))
    # declare the word to check
    get_word = random_word().lower()
    largest = 0
    trial = 10
    track = {}
    my_word = []
    # play game if user response is option 1
    if entry_1 == 1:
        print("loading...\n")
        print("--------------- HANGMAN GAME IS READY TO PLAY", player_name, "---------------\n")
        # generate a while loop to evaluate the worst case scenario
        spaces = new_guess_output(get_word)
        while trial > 0:
            new = ''.join(spaces)
            # set condition to quit game automatically if the word is already completed
            if new == get_word:
                print("\n ================================================================\n|           CONGRATULATIONS", player_name, "...YOU WIN THE GAME         |\n|                        THE WORD IS =", get_word, "|\n ================================================================")
                break
            # get user input(letter)
            guess = input("\nGuess a letter: ").lower()
            new_word = reload(guess, get_word, spaces)
            print(new_word)
            # call the linear_search function
            result_1 = linear_search(get_word, guess)
            if guess == "quit":
                print("\nThanks for playing...")
                break
            # condition for if the result is not "None"
            if result_1 is not None:
                biggest = 0
                print("\nCORRECT LETTER :)\n")

                # track the repetition of each correct letter
                track[guess] = track.get(guess, 0) + 1
                # call the linear_search function
                result_2 = repeated(get_word, guess)
                # loop through my key-value pair to get my highest value to be compared
                for k, v in track.items():
                    if k == guess and (biggest == 0 or v > biggest):
                        biggest = v
                        if biggest <= result_2:
                            my_word.append(guess)
                        else:
                            print("'", guess, "' " "cannot be added to the word again...enter another letter")
                            my_word.append(guess)
                            my_word.remove(guess)
            elif result_1 is None:
                print("\nWRONG LETTER :(")
                trial -= 1
                print("\nYou have", trial, "more trials")
                if trial == 0:
                    print("\nUnfortunately", player_name, "you are out of trials")
                    print("\n =======================================\n|   YOU LOSE....THANKS FOR PLAYING...   |\n =======================================")
    # view instructions if user response is option 2
    elif entry_1 == 2:
        print("To play game\n============")
        print("\n1. You are to guess a letter at every round to see if it is in the hidden word")
        print("2. If your guessed letter is in the word after several trials, you win the game")
        print("3. If your guessed letter is not in the word after trial is complete, you loose")
    # quit game if user response is option 3
    elif entry_1 == 3:
        exit()
    else:
        print("Re-enter correct option")

