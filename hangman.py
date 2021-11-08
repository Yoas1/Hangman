import random
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_menu():
    print("""
      _    _                                         
     | |  | |                                         
     | |__| |  _ _ _ _     ___ _  _ _     ____ _____
     | |__| |/ _` | '_ \ / _` | '_  _ \  / _  | '_ _\ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ 
    MENU:
    
    (S)tart
    (Q)uit
    """)


def print_start_game(max_tries):
    print("\n   ---GAME START---\n")
    print("   Your tries is: ", max_tries, "\n\n\n\n")


def choose_word(file_path, index):
    d = dict()
    count_all_words = 0
    count_words = 0
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split(" ")
            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                    count_all_words += 1
                else:
                    d[word] = 1
                    count_words += 1
                    count_all_words += 1
    index = int(index % count_all_words) - 1
    return (words[index])


def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {0: '''
          h++y++++y
          d y     
          dy       
          d
          d
          d
          d
          d
          d
        ++m++ ''',
                      1: '''
          h++y++++y
          d y     d
          dy      o
          d
          d
          d
          d
          d
          d
        ++m++  ''',
                      2: '''
          h++y++++y
          d y     d
          dy      o
          d     o   o
          d      o o 
          d    
          d    
          d     
          d     
        ++m++  ''',
                      3: '''
          h++y++++y
          d y     d
          dy      o
          d     o   o
          d      o o 
          d       o 
          d       o  
          d      
          d     
        ++m++  ''',
                      4: '''
          h++y++++y
          d y     d
          dy      o
          d     o   o
          d      o o 
          d     o o 
          d    o  o  
          d      
          d     
        ++m++  ''',
                      5: '''
          h++y++++y
          d y     d
          dy      o
          d     o   o
          d      o o 
          d     o o o
          d    o  o  o
          d      
          d     
        ++m++  ''',
                      6: '''
          h++y++++y
          d y     d
          dy      o
          d     o   o
          d      o o 
          d     o o o
          d    o  o  o
          d      o 
          d     o   
        ++m++  ''',
                      7: '''
          h++y++++y
          d y     d
          dy      o
          d     o   o
          d      o o 
          d     o o o
          d    o  o  o
          d      o o
          d     o   o
        ++m++  '''}
    print(HANGMAN_PHOTOS[num_of_tries])
    return


def show_hidden_word(secret_word, old_letters_guessed):
    status = '\n   '
    for letter in secret_word:
        if letter in old_letters_guessed:
            status += letter + " "
        else:
            status += "_ "
    return status


def check_valid_input(letter_guessed, old_letters_guessed):
    if not letter_guessed.isalpha() and len(letter_guessed) > 1:
        return False
    elif letter_guessed.isalpha() and len(letter_guessed) > 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif letter_guessed.isupper:
        if letter_guessed in old_letters_guessed:
            return False
        elif letter_guessed not in old_letters_guessed:
            return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    try_update = check_valid_input(letter_guessed, old_letters_guessed)
    if try_update is False:
        print("X")
        print(*sorted(old_letters_guessed), sep=" -> ")
        return False
    elif try_update is True:
        old_letters_guessed += [letter_guessed.lower()]
        return True


def check_win(secret_word, old_letters_guessed):
    status = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            status += letter
        else:
            status += "_ "
    if status == secret_word:
        clear()
        print("""\n   ########   WIN!!!   ########""")
        return True
    else:
        return False


def main():
    clear()
    while True:
        print_menu()
        option = input("   Enter option:").lower()
        clear()
        if option == 's':
            MAX_TRIES = 7
            old_letters = []
            print_start_game(MAX_TRIES)
            enter_pate_select = input("""   (1) - Animals\n   (2) - fruits\n   Choose option:""")
            clear()
            enter_path = {"1": "animals", "2": "fruits"}
            file_upload = enter_path[enter_pate_select] + ".txt"
            print("   The category for guessing is: ", enter_path[enter_pate_select])
            with open(file_upload, 'r') as file:
                content = file.read()
                content_list = content.split(" ")
                file.close()
            pick_a_number = random.randint(1, len(content_list))
            num_of_tries = 0
            print_hangman(num_of_tries)
            print("   Have to guess:\n " + show_hidden_word(choose_word(file_upload, pick_a_number), old_letters))
            while num_of_tries <= MAX_TRIES:
                letter_guessed_user = input("\n   Guess a letter:").lower()
                if not try_update_letter_guessed(letter_guessed_user, old_letters):
                    continue
                if "_ " in (show_hidden_word(choose_word(file_upload, pick_a_number), old_letters)):
                    if letter_guessed_user in choose_word(file_upload, pick_a_number):
                        show_hidden_word(choose_word(file_upload, pick_a_number), old_letters)
                        print("   Your tries is: ", 7 - num_of_tries)
                    elif num_of_tries == 6:
                        clear()
                        print_hangman(7)
                        print("   LOSE!!!")
                        break
                    else:
                        clear()
                        print("   :(")
                        num_of_tries += 1
                        print_hangman(num_of_tries)
                        show_hidden_word(choose_word(file_upload, pick_a_number), old_letters)
                        print("   Your tries is: ", 7 - num_of_tries)
                elif check_win(choose_word(file_upload, pick_a_number), old_letters):
                    print("\n   The word is: " + show_hidden_word(choose_word(file_upload, pick_a_number), old_letters))
                    break
                print(show_hidden_word(choose_word(file_upload, pick_a_number), old_letters))

        elif option == 'q':
            break
        else:
            print("   Error: invalid option")


if __name__ == "__main__":
    main()

