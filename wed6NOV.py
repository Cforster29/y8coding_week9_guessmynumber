print("you have 5 guesses!")
import random
from random import randint
correct = random.randint(1,100)
i = 1
number = None

while number != correct:
    number = print(int(input("What Is MY nUMBEr?")))
    number = number
    five_less = correct - 5
    five_more = correct + 5
    if number > correct:
        print("LOWER!")
    if number < correct:
        print("HIGHER!")
    if number == five_less:
        print("CORRECT ANSWER IN RANGE OF 5")
    if number == five_more:
        print('CORRECT ANSWER IN RANGE OF 5')
    if number == correct:
        print("correct!")