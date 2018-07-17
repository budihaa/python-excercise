# Guessing game Mini Project

from random import randint

answer = randint(1, 10)

# while True -> create endless loop
while True:
    ask_number = int(input('Guess the number between 1 - 10: '))
    if ask_number > answer:
        print('Too high. Guess again!')
    elif ask_number < answer:
        print('Too low. Guess again!')
    else:
        print("You won!")
        ask_again = input('Wanna play again? (y/n): ')
        if ask_again == "y":
            ask_number = int(input('Guess the number between 1 - 10: '))
        elif ask_again == "n":
            print("Okay bye!")
            break
