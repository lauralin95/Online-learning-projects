# send to philip.de-grouchy@city.ac.uk

import random

def select_word():
    openfile = open('words.txt', 'r')
    infile = openfile.read()
    openfile.close()
    words = infile.split('\n')
    wordpos = random.randint(0, len(words)-1)
    guess_word = list(words[wordpos])
    return guess_word


def checkword():
    guess_word = select_word()
    # print(guess_word)
    hidden_word = guess_word[:]
    hidden_word = ['*' for x in hidden_word]
    user_input_record = []
    numberoftries = 6
    # print(numberoftries)
    while True:
        if ''.join(hidden_word) == ''.join(guess_word):
            return print('You did it! The word is', ''.join(hidden_word))
            break
        elif numberoftries == 0 and ''.join(hidden_word) != ''.join(guess_word):
            missedtimes = len([letter for letter in hidden_word if letter == '*'])
            return print('The word is', ''.join(guess_word) + '.', 'You missed by', missedtimes, 'letters.')
            break
        elif numberoftries != 0 and ''.join(hidden_word) != ''.join(guess_word):
            letter = 'Enter a letter in word ' + str(''.join(hidden_word)) + ' > '
            user_input = input(letter)
            if user_input in guess_word:
                if user_input not in user_input_record:
                    for pos in range(len(guess_word)):
                        if guess_word[pos] == user_input:
                            hidden_word[pos] = user_input
                elif user_input in user_input_record:
                    print('You have already entered', user_input)
            else:
                print(user_input, 'is not in the word')
                numberoftries = numberoftries - 1
                print('You have', numberoftries, 'tries left.')
            user_input_record.append(user_input)

def main():
    print('Hangman game: you are allowed 6 misses.')
    checkword()
    user_input = input('Do you want to play again? (Y or N) ')
    while user_input.lower() != 'q':
        if user_input.lower() == 'y':
            checkword()
            user_input = input('Do you want to play again? (Y or N) ')
        elif user_input.lower() == 'n':
            print('Thanks for playing!')
            break

main()

