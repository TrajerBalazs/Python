#To control the times a while loop repeats, we start with a variable set to a number. We call this variable a counter variable.

counter = 1

#Then we use a comparison in the condition to compare the counter variable to a number. In this case, counter < 4:.
#Inside the code block, we make the condition return False and stop the loop by incrementing the counter variable.
#In this case += increases the values of the counter variable by 1 each time the loop runs. Try it with counter += 1.

counter = 1

while counter < 4:
    print(counter)
    counter += 1
print("--------------------------------------------------")

#Changing the conditions tells the loop when to stop. For example, changing the condition to counter < 10.

counter = 1

while counter < 10:
    print(counter)
    counter += 1
print("--------------------------------------------------")

#Changing the counter variable's value changes when the loop starts. Like setting counter to 5.

counter = 5

while counter < 10:
    print(counter)
    counter += 1
print("--------------------------------------------------")

#The order of your code affect what the console displays. Place counter += 1 first, to display 6 to 10.

counter = 5

while counter < 10:
    counter += 1
    print(counter)
    