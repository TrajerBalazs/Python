#----------------------------------------------------------------------------------------------------------------------------------------


#We know how to repeat code using a while loop. Like this program repeating statements to display The American Flag.

first_counter = 0

while first_counter < 5:
    print("**********---------")
    first_counter += 1

second_counter = 0

while second_counter < 4:
    print("-------------------")
    second_counter += 1

#----------------------------------------------------------------------------------------------------------------------------------------


#Using for loops, we can write programs with much less code and make it easier for other programmers to understand.

for i in range(4):
    print("**********---------")
for i in range (5):
    print("-------------------")

#----------------------------------------------------------------------------------------------------------------------------------------


#To create a for loop like this, we add the for keyword, a variable like i, the word in and finaly range():
#In a for loop we can specify how many times we'd like our loop to run with the range() statement.

for i in range(5):
    print("Happy Birthday to you!")

#----------------------------------------------------------------------------------------------------------------------------------------


#Adding a number like 6, inside range() means it'll loop over the code block 6 times, from 0 until 5.

for i in range(6):
    print(i)

#----------------------------------------------------------------------------------------------------------------------------------------


#The variable before in, in this case, i, is the counter variable. It counts what repetition of the loop we're currently on.

for i in range(3):
    print(i)
    print("For loops are great!")