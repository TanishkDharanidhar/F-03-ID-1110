import random
def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)
    

