#one way to repeat lines of codes is to write them over and over again, but it takes a really long time if we want to create larger programs.

print("and again")
print("and again")
print("and again")
print("and again")
print("and again")
print("and again")

#To build larger programs and websites, we repeate lines of code using a while loop. 
#Using a while loop to repeat lines of code starts with the while keyword.
#A while loop repeats its code block while its condition is True. We code a True condition with True followed by a colon :.
#The code the while loop repeats comes after the :, inside the indented code block. Like the print() statement here.
#If a while loop's condition stays True forever, we call it an infinite loop since it will loop infinitely, like with print() here.

while True:
    print("and again")
    break

#So far we've learned how to create a while loop, now let's focus on how to stop them for looping infinitely.
#To stop a loop, we start by creating a variable outside the loop. 

keep_going = True

while keep_going == True:
    print("and again")
    keep_going = False

#The loop runs its entire code block because keep_going is True at first, but doesn't run again if we set keep_going to False.

keep_going = True

while keep_going == True:
    print("and again")
    keep_going = False

    print("One more time")