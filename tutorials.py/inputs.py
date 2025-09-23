#Programs are more fun if they can take input from the outside.
#When we run a code, we cab uinclude the input to alter the programs. 

#The order of the instructions matters. Once we collect input and store it in a variable, we can reuse it. 

print("What's your name?")
name_input = input()
print(f"Hi, {name_input}!") 

#To gather input from a user in a Python program, we use the input function. The user's input can then be assigned to a variable.

user_input = input()

#After capturing input, we can assign it to a variable and use it just as any other variable.

print("What's your name?")
name_input = input()
print(f"Hi, {name_input}!") 

#We can also add an additional prompt to the input function. The prompt will be displayed in the console. 

user_input = input("Enter your name : ")

#If we enter an additional prompt, the user will start typing at the same line as the prompt is displayed in the console. 
#That's why it's helpful to add a whitespace at the end of the prompt used in the input function.

user_input = input("Enter your name: ")
print(f"Thanks, {user_input}")

#We can also use the input function as many times as we want. 

user_input_1 = input("Enter a number: ")
user_input_2 = input("Enter another number: ")
print(user_input_1)
print(user_input_2)

#The input is always of type string. If we want to use it as a number, we need to convert it to an integer or float beforehead.

user_input_1 = input("Enter a number: ")
user_input_2 = input("Enter another number: ")
number1 = int(user_input_1)
number2 = int(user_input_2)
result = number1 + number2
print(f"The sum is {result}")