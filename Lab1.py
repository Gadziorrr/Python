# Zadanie 1

# from random import randint  # import dzieje się tylko raz
#import time

# def throw():
#     return randint(1, 6) + randint(1, 6)


# def single_game():
#     print("Rzucam...")
#     time.sleep(1)
#     firstThrow = throw()
#     print(f"Wypadła suma równa: {firstThrow}")

#     if firstThrow in (7, 11):
#         print("Wygrana!")
#         return True
#     elif firstThrow in (2, 3, 12):
#         print("Przegrana!")
#         return False
#     else:
#         print(f"Punkt: {firstThrow}")
#         while True:
#             print("Rzucam...")
#             time.sleep(1)
#             secondThrow = throw()
#             print(f"Wypadła suma równa: {secondThrow}")

#             if secondThrow == firstThrow:
#                 print("Wygrana!")
#                 return True
#             elif secondThrow == 7:
#                 print("Przegrana!")
#                 return False
#             else:
#                 continue


# def get_answer(question):
#   while True:
#     answer = input(question).lower()
#     if answer in ('tak', 't', 'yes', 'y'):
#       return True
#     elif answer in ('nie', 'n', 'no'):
#       return False
#     else:
#       print("Błędna odpowiedź! Odpowiedz 'Tak' lub 'nie'!")


# def main():
#   wins = 0
#   loses = 0

#   while True:
#     if single_game():
#       wins += 1
#     else:
#       loses += 1
#     if (get_answer("Czy chcesz zagrać jeszcze raz? \n")):
#       continue
#     else:
#       print("Dziękuję za grę!")
#       print(f"Wygrane: {wins}")
#       print(f"Przegrane: {loses}")
#       return


# main()


# Zadanie 2

# from random import choice

# class Coin:
#     side: str = None

#     def __init__(self):
#         self.side = choice(['orzeł', 'reszka'])

#     def __str__(self):
#         print(self.side)

#     def throw(self):
#         self.side = choice(['orzeł', 'reszka'])


# def start_game():
#     c1 = Coin()
#     c2 = Coin()
#     c5 = Coin()

#     money: int = 0

#     while True:
#         c1.throw()
#         c2.throw()
#         c5.throw()

#         if (c1.side == 'orzeł'):
#             money += 1
#         if (c2.side == 'orzeł'):
#             money += 2
#         if (c5.side == 'orzeł'):
#             money += 5

#         if money == 20:
#             return True
#         elif money > 20:
#             return False
#         else:
#             continue


# def main():
#   wins = 0
#   for i in range (0, 1000):
#     if(start_game()):
#         wins += 1

#   print(f"Liczba wygranych wynosi {wins}")

# main()


# Zadanie 3
from random import randint


class Die:
    def __innit__(self, sides, value=None):
        self._sides = sides
        self._value = value

    def roll(self):
        self._value = randint(1, self._sides)

    def get_sides(self):
        return self._sides

    def get_value(self):
        return self._value

    def __str__(self):
        return f'Liczba ścianek to {self._sides}, \
               a liczba oczek wynosi {self._value}'


def main():
    firstDie = Die(6)
    secondDie = Die(5)
