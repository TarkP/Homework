import random

number = random.randint(1, 10)
print ("try to guess the number between 1 to 10 in 3 guesses")

guess1 = int(input("\nEnter your first guess:"))
if guess1 == number:
    print("you guessed correct, on your first try")
elif guess1 > number:
    print ("your guess was too high")
else:
    print ("your guess was too low")

guess2 = int(input("\nEnter your second guess:"))
if guess2 == number:
    print("you guessed correct, on your second try")
elif guess2 > number:
    print ("your guess was too high")
else:
    print ("your guess was too low")


guess3 = int(input("\nEnter your third guess:"))
if guess3 == number:
    print("you guessed correct, on your third try")
elif guess3 > number:
    print ("your guess was too high")
else:
    print ("your guess was too low")
    #task 2
    name = input("What's your name?!?!?!?!?!!?")
    age = int(input("AND YOUR AGE?????????"))
    myAge = age + 1
#task 3
from random import shuffle
text = input("enter a text")
for i in range(5):
    l = list(text)
    shuffle(l)
    result = ''.join(l)
    print(result
#task 4
from random import randint
num1 = randint (2,10)
num2 = randint (2,10)
result = num1 + num2
answer=input(f"give an answer {num1} + {num2} equals?")
if result == answer:
 print ("good answer")

