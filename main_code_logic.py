from colorama import Fore, Back, Style
def word_check(user_word,correct_word):
    user_word = user_word.lower()
    green_count = 0
    yellow_count = 0
    cyan_count = 0 
    user_word_check = ''
    for i,c in enumerate(user_word):
        if c in correct_word:
            if user_word[i] == correct_word[i]:
                green_count += 1 #change colour of letter
                temp = Fore.WHITE + Back.GREEN + user_word[i]
                user_word_check += temp
            else:
                yellow_count += 1
                temp = Fore.BLUE + Back.YELLOW + user_word[i]
                user_word_check += temp
        else:
            cyan_count += 1
            temp = Fore.WHITE + Back.CYAN + user_word[i]
            user_word_check += temp
    return f'{user_word_check}{Style.RESET_ALL}'
user_word = 'Hbppa'
correct_word = 'happy'
print(word_check(user_word,correct_word))
print('abc')
