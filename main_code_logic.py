from colorama import Fore, Back, Style
import random

#function to assign background colours to letters
def word_check(user_word,correct_word):
    user_word = user_word.lower()
    user_word_check_list = []
    correct_word_list = []
    user_word_check = ''
    
    for letter in correct_word:
        correct_word_list.append(letter)

    for i,c in enumerate(user_word):
        if c in correct_word:
            if user_word[i] == correct_word[i]:
                #the letter is in the word and correct place
                temp = Fore.WHITE + Back.GREEN + user_word[i] + ' ' 
                user_word_check_list.append(temp)
            else:
                #the letter is in the word and not in correct place
                temp = Fore.BLUE + Back.YELLOW + user_word[i]+ ' ' 
                user_word_check_list.append(temp)
        else:
            #the letter is not in the word
            temp = Fore.WHITE + Back.CYAN + user_word[i]+ ' '  
            user_word_check_list.append(temp)
    
    #removing green letters
    for i,c in enumerate(user_word):
        if c in correct_word:
            if user_word[i] == correct_word[i]:
                correct_word_list.remove(c)

    #if letter occurs twice in user word but not correct word, one of the extra letters should be cyan 
    for i,c in enumerate(user_word):
        if c in correct_word:
            if user_word[i] != correct_word[i]:
                if c not in correct_word_list:
                    temp = Fore.WHITE + Back.CYAN + user_word[i]+ ' '
                    user_word_check_list[i] = temp

    #converting list to string
    for i in user_word_check_list:
        user_word_check += i

    return f'{user_word_check}{Style.RESET_ALL}' #returning the checked word and resetting style

#function to check number of green letters
def color_count(user_word,correct_word):
    user_word = user_word.lower()
    green_count = 0
    
    for i,c in enumerate(user_word):
        if c in correct_word:
            if user_word[i] == correct_word[i]:
                green_count += 1

    return green_count

#checking if user word has only alphabets
def alphachecker(user_word):
    user_word = user_word.lower()
    alpha_count = 0

    for i in user_word:
        if i.isalpha():
            alpha_count += 1

    if alpha_count == len(user_word):
        return True
    else:
        return False

#getting a random word for correct word
def random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

#getting a random word for hint
def hint_random_word():
    with open("random_word_hint.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)


play = True

#play again loop
while play:
    keyb_pre = {}
    letter_colour = {}
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in letters:
        letter_colour[i] = 0

    for i in range(1, 27):  #ASCII 65-90 upper case
        key = i
        value = chr(i + 64)  # Convert the number to its corresponding uppercase alphabet ASCII value
        keyb_pre[key] = value
    keyb = keyb_pre

    #creating a wordle keyboard like format
    def keyboard(user_word,correct_word):
        global keyb
        global letter_colour
        user_word = user_word.lower()

        for i,c in enumerate(user_word):
            if c in correct_word:
                if user_word[i] == correct_word[i]:
                    letter_colour[c] = 'green'
                    temp = Fore.WHITE + Back.GREEN + user_word[i].upper() + Style.RESET_ALL
                    keyb[(ord(user_word[i]) - 96)] = temp
                
                else:
                    #if a letter is already green dont change it
                    if letter_colour[c]  == 'green':
                        temp = Fore.WHITE + Back.GREEN + user_word[i].upper() + Style.RESET_ALL
                    else:
                        letter_colour[c] = 'yellow'
                        temp = Fore.BLUE + Back.YELLOW + user_word[i].upper() + Style.RESET_ALL
                    keyb[(ord(user_word[i]) - 96)] = temp
            
            else:
                letter_colour[c] = 'cyan'
                temp = Fore.WHITE + Back.CYAN + user_word[i].upper() + Style.RESET_ALL
                keyb[(ord(user_word[i]) - 96)] = temp

        return f"{keyb[17]}  {keyb[23]}  {keyb[5]}  {keyb[18]}  {keyb[20]}  {keyb[25]}  {keyb[21]}  {keyb[9]}  {keyb[15]}  {keyb[16]}\n {keyb[1]}  {keyb[19]}  {keyb[4]}  {keyb[6]}  {keyb[7]}  {keyb[8]}  {keyb[10]}  {keyb[11]}  {keyb[12]}\n  {keyb[26]}  {keyb[24]}  {keyb[3]}  {keyb[22]}  {keyb[2]}  {keyb[14]}  {keyb[13]}"


    guess_number = 0
    correct_word = random_word()
    
    print('Enter 5-letter word.')
    print("If you need help during an attempt, type 'help'.")
    
    while guess_number < 6:
        user_word = input()[:5]

         #help menu: random word, vowels present, starting letter, ending letter
        if user_word == 'help':
            print('1 Random Word: Get a random word from a list of words.\n2 Vowels Present: Get the vowels present in the answer.\n3 Starting Letter: Get the starting letter of the answer.\n4 Ending Letter: Get the ending letter of the answer.')
            
            hint_response = input('Type number: ')
            
            if hint_response == '1':
                #random word
                print("Random word = ",hint_random_word().lower())
                continue
            
            elif hint_response == '2':
                #vowels present
                vowels = 'aeiou'
                correct_word_vowels = ''
                
                for i in correct_word:
                    if i in vowels:
                        temp = i.upper() + ' '
                        correct_word_vowels += temp
                        
                print('Vowels present: ', correct_word_vowels)
                continue
            
            elif hint_response == '3':
                #starting letter
                print('Starting letter: ', correct_word[0])
                continue
            
            elif hint_response == '4':
                #ending letter
                print('Ending letter: ', correct_word[-1])
                continue
        
        else:
            #eliminating non-alphabet word error
            if alphachecker(user_word) == False:
                print(f'{user_word} Word should contain only alphabets. Try again.')
                continue

            #eliminting less than 5-letter user word error 
            if len(user_word) < 5:
                print(f'{user_word} Please enter 5-letter word. Try again.')
                continue


            check = word_check(user_word, correct_word)
            print(check)
            print(keyboard(user_word,correct_word))

            #chechking if the current user word is the correct word
            correct_answer_check = color_count(user_word, correct_word)
            if correct_answer_check == 5:
                print('Correct answer!')
                break
            else:
                guess_number += 1


    if guess_number == 6:
        print(f"Your 6 guesses are over. It was '{correct_word}'.")

    response = input("Do you want to play again? Type 'yes' or 'no'.\n")
    
    if response == 'no':
        play = False
