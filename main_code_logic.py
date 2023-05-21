from colorama import Fore, Back, Style
def word_check(user_word,correct_word):
    user_word = user_word.lower()
    #green_count = 0
    #yellow_count = 0
    #cyan_count = 0
    user_word_check = ''
    for i,c in enumerate(user_word):
        if c in correct_word:
            if user_word[i] == correct_word[i]:
                #green_count += 1 ,change colour of letter
                temp = Fore.WHITE + Back.GREEN + user_word[i] + ' '
                user_word_check += temp
            else:
                #yellow_count += 1
                temp = Fore.BLUE + Back.YELLOW + user_word[i]+ ' '
                user_word_check += temp
        else:
            #cyan_count += 1
            temp = Fore.WHITE + Back.CYAN + user_word[i]+ ' '
            user_word_check += temp
    return f'{user_word_check}{Style.RESET_ALL}'
def color_count(user_word,correct_word):
    user_word = user_word.lower()
    green_count = 0
    yellow_count = 0
    cyan_count = 0
    for i,c in enumerate(user_word):
        if c in correct_word:
            if user_word[i] == correct_word[i]:
                green_count += 1 #change colour of letter
            else:
                yellow_count += 1
        else:
            cyan_count += 1
    return (green_count, yellow_count, cyan_count)#change to list if error
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
guess_number = 0
print('Enter 5-letter word.')
while guess_number < 6:
    user_word = input()[:5] # TODO: error handling
    if len(user_word) < 5:
        print(f'{user_word} Please enter 5-letter word. Try again.')
        continue
    check = word_check(user_word, correct_word)
    print(check)
    correct_answer_check = color_count(user_word, correct_word)
    if correct_answer_check[0] == 5:
        print('Correct answer!')
        break
    else:
        guess_number += 1
if guess_number == 6:
    print(f"Your 6 guesses are over. It was '{correct_word}'.")
