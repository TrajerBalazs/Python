import random

number = random.randint(1,100)

moves = 0
tipp = 0

print("I thought of a number from 1 to 100.\n Guess it!\n")

while tipp!=number:
    tipp=int(input("I need a guess : "))
    moves += 1
    if number>tipp:
        print("I think its bigger!")
    if number<tipp:
        print("I think a smaller one!")

print(f"\n Congrats! {moves} moves u got it.")
