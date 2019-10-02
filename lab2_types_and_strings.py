#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        # print only first and last of the sentence
        print(message[0] + ' ' + message[len(message)-1])

        # use slice notation
        print(message[0: len(message)])

        # escaping a character
        print(message[0:3]+message[4:len(message)])

        # find all a's in the input word and count how many there are
        print(message.count("a's", 0, len(message)))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        print(message.replace('a', '-'))


        # printing only characters at even index positions
        print(message[2: len(message): 2])

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        list_input = list(message)
        print(list_input)

        # append a new element to the list and print
        list_input.append('a')
        print(list_input)

        # remove from the list in 3 ways
        # way 1
        del list_input[0]
        print(list_input)
        # way 2
        list_input.pop(3)
        print(list_input)
        # way 3
        list_input.remove('a')
        print(list_input)

        # check if the word cake is in your input list
        print('c'and 'a' and 'k' and 'e' in list_input)

        # reverse the items in the list and print
        list_input.reverse()
        print(list_input)

        # reverse the list with the slicing trick
        print(list_input[::-1])

        # print the list 3 times by using multiplication
        print(list_input * 3)



tas = Types_and_Strings()
tas.play_with_lists()
#tas.play_with_lists()