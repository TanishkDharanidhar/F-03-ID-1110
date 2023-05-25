from colorama import Fore,Back,Style
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
   return f"{keyb[17]}  {keyb[23]}  {keyb[5]}  {keyb[18]}  {keyb[20]}  {keyb[25]}  {keyb[21]}  {keyb[9]}  {keyb[15]}  {keyb[16]}\n {keyb[1]}  {keyb[19]}  {keyb[4]}  {keyb[6]}  {keyb[7]}  {keyb[8]}  {keyb[10]}  {keyb[11]}  {keyb[12]}\n  {keyb[26]}  {keyb[24]}  {keyb[3]}  {keyb[22]}  {keyb[2]}  {keyb[14]}  {keyb[13]}"