# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        list_input = self.user_input.split()
        i = 0
        while i < len(list_input):
            word = list(list_input[i])
            if len(word) > 2:
                index_1 = 1
                index_2 = 2
                temp = word[1]
                while index_2 <= len(word)-2:
                    word[index_1] = word[index_2]
                    word[index_2] = temp
                    index_2 += 2
                    index_1 += 2
                    temp = word[index_1]
            list_input[i] = ''.join(word)
            i += 1
        self.user_input = ' '.join(list_input)

        print("The scramble input is: ", self.user_input)

        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

word_scrambler = WordScramble()
word_scrambler.scramble()

