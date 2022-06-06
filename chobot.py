import random

wordlist = open("words.txt", "r")

random_word = random.choice(wordlist.readlines())
wordlist.close()
print(random_word)
