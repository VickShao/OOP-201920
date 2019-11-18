# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 07-11-2019
# purpose: Lab 7 - Word Games

class WordGames:
    def __init__(self):
        self.mywords = input("Please enter a word or sentence: ")
        self.word_play()

    def word_play(self):
        print("User input was: "+self.mywords)

class WordDupli(WordGames):
    def __init__(self):
        super(WordDupli, self).__init__()
        self.Dupli()

    def Dupli(self):
        list_input = self.mywords.split()
        new_list = []
        i = 0
        while i < len(list_input):
            new_list.append(list_input[i])
            new_list.append(list_input[i])
            i += 1
        self.mywords = ' '.join(new_list)
        print("The dupli input is: ", self.mywords)


class WordScramble(WordGames):
    def __init__(self):
        super(WordScramble, self).__init__()
        self.Scramble()

    # first scramble is just one word
    def Scramble(self):
        list_input = self.mywords.split()
        i = 0
        while i < len(list_input):
            word = list(list_input[i])
            if len(word) > 2:
                index_1 = 1
                index_2 = 2
                temp = word[1]
                while index_2 <= len(word) - 2:
                    word[index_1] = word[index_2]
                    word[index_2] = temp
                    index_2 += 2
                    index_1 += 2
                    temp = word[index_1]
            list_input[i] = ''.join(word)
            i += 1
        self.mywords = ' '.join(list_input)

        print("The scramble input is: ", self.mywords)

wg = WordDupli()