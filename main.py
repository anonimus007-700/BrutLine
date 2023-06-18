import itertools

class BrutLine:
    def __init__(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_")
        self.number = list("0123456789")

        self.start = int(input("Enter a starting position of 0: "))
        self.passworld = input("Enter a password to guess: ")

    def full_bruteforce(self):
        for length in itertools.count(start=self.start):
            combinations = itertools.product(self.alphabet, repeat=length)

            for combination in combinations:
                word = "".join(combination)
                print(word)
                if self.passworld == word:
                    return word

    def number_bruteforce(self):
        for length in itertools.count(start=self.start):
            combinations = itertools.product(self.number, repeat=length)

            for combination in combinations:
                word = "".join(combination)
                if self.passworld == word:
                    return word
