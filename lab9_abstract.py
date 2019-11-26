from abc import ABC, abstractmethod

class entire_game(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_num(self):
        pass

class fibonacci(entire_game):
    def __init__(self):
        self.get_num()
        self.output_num()
        self.game()
    
    def get_num(self):
        self.count = int(input("Please type in a number: "))

    def output_num(self):
        print("Fibonacci numbers are: %d" %self.count)

    def game(self):
        array = [0,1]
        i = 2
        while i <= self.count:
            array.append(array[i-1] + array[i-2])
            i += 1
        print("Fibonacci Sequence:",end='')
        print(array)

g = fibonacci()
