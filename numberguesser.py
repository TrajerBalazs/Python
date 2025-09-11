import random

number = random.randint(1,100)

moves = 0
guess = 0

print("I thought of a number from 1 to 100.\n Guess it!\n")

while guess!=number:
    guess=int(input("I need a guess : "))
    moves += 1
    if number>guess:
        print("It's bigger!")
    if number<guess:
        print("It's smaller!")

print(f"\n Congrats! {moves} moves u got it.")
