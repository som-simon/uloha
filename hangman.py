# from wordle_list import Word_list
import random
# import os


def hangman_word(word, guesses):
    pr_w = ""
    for i in word:
        if i in guesses:
            pr_w += i

        else:
            pr_w += '_'

    return pr_w


def game(ran_w, guess_n):

    guesses = set()
    wrong_let = 0

    print(hangman_word(ran_w, guesses))
    print()

    while guess_n:
        guess = input('guess letter: ').lower()
        print()

        if len(guess) == 5:
            if guess == ran_w:
                return True, wrong_let
            else:
                return False, wrong_let
        elif not(guess in guesses) and (guess in ran_w):
            guesses.add(guess)
        elif not(guess in guesses):
            guesses.add(guess)
            wrong_let += 1
            guess_n -= 1
        else:
            print('already used this letter')
            wrong_let += 1
            guess_n -= 1

        f = hangman_word(ran_w, guesses)

        print(f)
        print("guesses: " + ', '.join(guesses))
        print()

        if '_' in f:
            pass
        else:

            return True, wrong_let
    return False, wrong_let


if __name__ == "__main__":
    # while True:
    #     difficulty = input('hard or easy? ').lower()

    #     if difficulty == "hard":
    #         random_word = random.choice(Word_list.possible_try)
    #         break
    #     elif difficulty == "easy":
    #         random_word = random.choice(Word_list.wordlist)
    #         break
    #     else:
    #         print('enter valid difficulty')

    choise = input("print random word? y/N ").lower()
    wordlist = open("words.txt", "r")

    random_word = str(random.choice(wordlist.readlines()))[0:-1]
    if choise == 'y':
        print(r"{}".format(random_word))
    else:
        pass

    wordlist.close()

    guess_num = 9

    print()
    print(f"max number of wrong guesses: {guess_num}")
    print("you can always type the whole word, either win or lose")

    t = game(random_word, guess_num)

    if t[0]:
        print(f'you won, the word was: {random_word}')
        print(f"number of wrong guesses: {t[1]}")
    else:
        print(f'you lost, the word was: {random_word}')
        print(f"number of wrong guesses: {t[1]}")
        print()
