"""
Import the display module to the login page, then import all the login modules
"""
from display_module import *
from login_module import *
from prison_module import *
from check_module import *


# call display to be the header for the login page
display()
while True:
    details()
    try:
        # get user response for option above
        val = int(input("\nEnter a value: "))

        # perform some functions if user enters 1
        if val == 1:
            display()
            new_reg()
            try:
                # get user response for option above
                reg_val = int(input("\nEnter a value for registration: "))
                if reg_val == 1:
                    # perform some functions if user enters 1
                    display()
                    new_admin_reg()
                if reg_val == 2:
                    # perform some functions if user enters 2
                    display()
                    new_user_reg()
            except:
                print("---Invalid format---")

        if val == 2:
            display()
            # display general login page after display function is called
            general_login()
            # choose section to work with
            try:
                display()
                section()
                # get user response for option above
                entry_1 = int(input("\nEnter a section: "))
                # perform some functions if user enters 1
                if entry_1 == 1:
                    display()
                    admin_login()
                    display()
                    while True:
                        try:
                            add_view()
                            # add prisoner data and store it in a data file(Prisoner.txt) if user enters 1
                            entry_1a = int(input("\nEnter a data number: "))
                            # run this code if number is 1
                            if entry_1a == 1:
                                # collect prisoner full name, age, sex, height, crime committed, date of sentence, time duration, marital status, cell ID and cell number
                                while True:
                                    value_1 = input("\nAdd prisoner data(y/n): ")
                                    if value_1 == "y":
                                        display()
                                        view_prisoner_data()
                                        # get a cell ID for prisoner data to be added
                                        prisoner_id = random_id()
                                        print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCell ID generated: ", prisoner_id)
                                        f_name = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter first name: ").upper()
                                        l_name = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter last name: ").upper()
                                        sex = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Sex: ").upper()
                                        dob = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Date of birth: ")
                                        height = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter height(cm): ")
                                        marital_status = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter marital status: ").upper()
                                        crime_committed = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter crime committed: ")
                                        date_of_sentence = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter date of sentence: ")
                                        time_duration = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter time duration(months): ")
                                        cell_no = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter cell number: ").upper()
                                        tm = time.ctime()
                                        print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", tm)
                                        prisoner_data(prisoner_id, f_name, l_name, sex, dob, height, marital_status, crime_committed, date_of_sentence, time_duration, cell_no, tm)
                                        prisoner_data_backup(prisoner_id)
                                    if value_1 == "n":
                                        break
                            # run this code if number is 2
                            if entry_1a == 2:
                                display()
                                while True:
                                    value_1 = input("\nAdd visitor data(y/n): ")
                                    if value_1 == "y":
                                        display()
                                        view_visitor_data()
                                        # get a cell ID for visitor data to be added
                                        visitor_id = random_id()
                                        print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCell ID generated: ", visitor_id)
                                        f_name = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter first name: ").upper()
                                        l_name = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter last name: ").upper()
                                        sex = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Sex: ").upper()
                                        phone_num = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter phone number: ")
                                        while True:
                                            try:
                                                visit()
                                                reason = int(input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter reason for visit: "))
                                                if reason == 1:
                                                    reason_for_visit = "DELEGATE_VISITATION"
                                                    break
                                                if reason == 2:
                                                    reason_for_visit = "INSPECTION_VISITATION"
                                                    break
                                                if reason == 3:
                                                    reason_for_visit = "MAINTENANCE_VISITATION"
                                                    break
                                                if reason == 4:
                                                    reason_for_visit = "PRISONER_VISITATION"
                                                    break
                                            except:
                                                print("---Invalid format---")
                                        date_of_visit = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter date of visit: ")
                                        tm = time.ctime()
                                        print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", tm)
                                        visitor_data(visitor_id, f_name, l_name, sex, phone_num, reason_for_visit, date_of_visit, tm)
                                        visitor_data_backup(visitor_id)
                                    if value_1 == "n":
                                        break
                            # run this code if number is 3
                            if entry_1a == 3:
                                display()
                                view_prisoner()
                                while True:
                                    try:
                                        view = int(input("\nEnter a view number: "))
                                        if view == 1:
                                            display()
                                            view_prisoner_id()
                                            one_prisoner_data()
                                            break
                                        if view == 2:
                                            display()
                                            data_prisoner()
                                            all_prisoners_data()
                                            break
                                    except:
                                        print("---Invalid format---")
                            # run this code if number is 4
                            if entry_1a == 4:
                                display()
                                view_all_visitor()
                                while True:
                                    try:
                                        view = int(input("\nEnter a view number: "))
                                        if view == 1:
                                            display()
                                            vi_id()
                                            one_visitor_data()
                                            break
                                        if view == 2:
                                            display()
                                            da_vi()
                                            all_visitors_data()
                                            break
                                    except:
                                        print("---Invalid format---")
                            # run this code if number is 5
                            if entry_1a == 5:
                                quit()
                        except:
                            print("---Invalid format---")
                if entry_1 == 2:
                    display()
                    user_login()
                    display()
                    while True:
                        pris_vis()
                        try:
                            entry_1b = int(input("\nEnter a data number: "))
                            # run this code if number is 1
                            if entry_1b == 1:
                                display()
                                view_pris()
                                while True:
                                    try:
                                        view = int(input("\nEnter a view number: "))
                                        if view == 1:
                                            display()
                                            pri_id()
                                            one_prisoner_data()
                                            break
                                        if view == 2:
                                            display()
                                            da_pri()
                                            all_prisoners_data()
                                            break
                                    except:
                                        print("---Invalid format---")
                            # run this code if number is 2
                            if entry_1b == 2:
                                display()
                                view_vi()
                                while True:
                                    try:
                                        view = int(input("\nEnter a view number: "))
                                        if view == 1:
                                            display()
                                            vi_id()
                                            one_visitor_data()
                                            break
                                        if view == 2:
                                            display()
                                            da_vi()
                                            all_visitors_data()
                                            break
                                    except:
                                        print("---Invalid format---")
                                    break
                        except:
                            print("---Invalid format---")
                        break
            except:
                print("---Invalid format---")
        if val == 3:
            while True:
                # using loops to check a value or letter in a word
                hangman_display()
                player_name = input("Enter player name: ").upper()
                # get user response for option above
                entry_1 = int(input("\nEnter a value from the listed option above: "))
                # declare the word to check
                get_word = random_word().lower()
                largest = 0
                b_points = 0
                points = 0
                trial = 10
                track = {}
                my_word = []
                # play game if user response is option 1
                if entry_1 == 1:
                    print("\nloading...\n")
                    print("--------------- HANGMAN GAME IS READY TO PLAY", player_name, "---------------\n")
                    # generate a while loop to evaluate the worst case scenario
                    spaces = new_guess_output(get_word)
                    while trial > 0:
                        new = ''.join(spaces)
                        # set condition to quit game automatically if the word is already completed
                        if new == get_word and points >= b_points:
                            b_points = points
                            print("\n ================================================================\n           CONGRATULATIONS", player_name, "...YOU WON THE GAME                \n                        THE WORD IS = '", get_word, "'                     \n                         BEST SCORE =", b_points, "\n================================================================")
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
                            points += 100
                            print("\nCORRECT LETTER :)\nSCORE ==", points)

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
                                        print("'", guess, "'cannot be added to the word again...enter another letter")
                                        my_word.append(guess)
                                        my_word.remove(guess)
                        elif result_1 is None:
                            points -= 100
                            print("\nWRONG LETTER :(\nSCORE ==", points)
                            trial -= 1
                            print("\nYou have", trial, "more trials")
                            if trial == 0:
                                print("\nUnfortunately", player_name, "you are out of trials")
                                print("\n =======================================\n|   YOU LOSE....THANKS FOR PLAYING...   |\n         SCORE =", points, "|\n|         BEST SCORE =", b_points, "|\n=======================================")
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
    except:
        print("---Invalid format---")

