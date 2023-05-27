from colorama import Fore, Back, Style
import random

def word_check(user_word,correct_word):
   user_word = user_word.lower() #converting all letters to lower case
   #green_count = 0
   #yellow_count = 0
   #cyan_count = 0
   user_word_check = ''
   for i,c in enumerate(user_word):
       if c in correct_word:
           if user_word[i] == correct_word[i]:
               #green_count += 1
               temp = Fore.WHITE + Back.GREEN + user_word[i] + ' ' #the letter is in the word and correct place, ' ' for space
               user_word_check += temp
           else:
               #yellow_count += 1
               temp = Fore.BLUE + Back.YELLOW + user_word[i]+ ' ' #the letter is in the word and not in correct place
               user_word_check += temp
       else:
           #cyan_count += 1
           temp = Fore.WHITE + Back.CYAN + user_word[i]+ ' '  #the letter is not in the word
           user_word_check += temp
   return f'{user_word_check}{Style.RESET_ALL}' #returning the checked word and resetting style


def color_count(user_word,correct_word):
   user_word = user_word.lower()
   green_count = 0
   yellow_count = 0
   cyan_count = 0
   for i,c in enumerate(user_word):
       if c in correct_word:
           if user_word[i] == correct_word[i]:
               green_count += 1
           else:
               yellow_count += 1
       else:
           cyan_count += 1
   return (green_count, yellow_count, cyan_count)#change to list if error


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

keyb_pre = {}
for i in range(1, 27):  #ASCII 65-90 upper case
   key = i
   value = chr(i + 64)  # Convert the number to its corresponding uppercase alphabet ASCII value
   keyb_pre[key] = value
keyb = keyb_pre

def keyboard(user_word,correct_word):
   global keyb
   user_word = user_word.lower()
   for i,c in enumerate(user_word):
       if c in correct_word:
           if user_word[i] == correct_word[i]:
               temp = Fore.WHITE + Back.GREEN + user_word[i].upper() + Style.RESET_ALL
               keyb[(ord(user_word[i]) - 96)] = temp
           else:
               temp = Fore.BLUE + Back.YELLOW + user_word[i].upper() + Style.RESET_ALL
               keyb[(ord(user_word[i]) - 96)] = temp
       else:
           temp = Fore.WHITE + Back.CYAN + user_word[i].upper() + Style.RESET_ALL
           keyb[(ord(user_word[i]) - 96)] = temp
   return f"{keyb[17]}  {keyb[23]}  {keyb[5]}  {keyb[18]}  {keyb[20]}  {keyb[25]}  {keyb[21]}  {keyb[9]}  {keyb[15]}  {keyb[16]}\n {keyb[1]}  {keyb[19]}  {keyb[4]}  {keyb[6]}  {keyb[7]}  {keyb[8]}  {keyb[10]}  {keyb[11]}  {keyb[12]}\n  {keyb[26]}  {keyb[24]}  {keyb[3]}  {keyb[22]}  {keyb[2]}  {keyb[14]}  {keyb[13]}"
#user_word = 'Hbppa'
correct_word = 'happy'
#print(word_check(user_word,correct_word))
#print('abc')
#a= Fore.WHITE + Back.GREEN + 'A'
#b= Fore.BLUE + Back.YELLOW + 'B'
#c= Fore.WHITE + Back.CYAN + 'C'
#return f string {Style.RESET_ALL}
# create menu
# words list, error handling(5-letter,string,all_alpha), keyboard colors

def random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

guess_number = 0
#correct_word = random_word()
print('Enter 5-letter word.')

while guess_number < 6:
   user_word = input()[:5] # TODO: error handling
   if alphachecker(user_word) == False:
       print(f'{user_word} Word should contain only alphabets. Try again.')
       continue
   if len(user_word) < 5:
       print(f'{user_word} Please enter 5-letter word. Try again.')
       continue
   check = word_check(user_word, correct_word)
   print(check)
   print(keyboard(user_word,correct_word))
   correct_answer_check = color_count(user_word, correct_word)
   if correct_answer_check[0] == 5:
       print('Correct answer!')
       break
   else:
       guess_number += 1

if guess_number == 6:
   print(f"Your 6 guesses are over. It was '{correct_word}'.")
#clean code
#add comments

