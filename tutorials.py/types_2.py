#We've seen the basic data types in Python - strings, integers, floats, and booleans. 

#If we are unsure of a value type, we can check it!
#Here, type() checks that is_ready is a bool, which is short for boolean.

is_ready = True
print(type(is_ready))

#We can get a variable's type using type() with the variable name. By adding print(), we can see the variable type in the console. 
is_ready = True
fuel_deposit = 59.89
best_grade = "A"
number_of_pets = 2
print(type(is_ready))
print(type(fuel_deposit))
print(type(best_grade))
print(type(number_of_pets))

#Python has built-in functions to convert data types. For example, int() helps us convert the age variable's string to an integer.

age = "17"
print(type(age))
converted_age = int(age)
print(type(converted_age))

print(converted_age < 18)

#The str() function allows us to take numerical values and convert them to strings. Convert the password variable to a string
# to compare to the old password. 

password = 980790
old_password = "81k29"

print(str(password) == old_password)

print(type(password))
print(type(old_password))

#If we use int() on a float value, we'll simply remove the decimal point and subsequent values. There will be no rounding. 

price = 9.90
print(int(price))

#Likewise, we can use float() on an integer. This will add a decimal point, and the ability to store fractional values. 

weeks = 12
print(float(weeks))

#If we use int() on a boolean, the equivalent numerical value will be 1 for True and 0 for False.
#Convert member and not_member to integers to check their new boolean values. 

member = True
not_member = False

value = int(member)
second_value = int(not_member)

print(value)
print(second_value)

#We can use bool() to convert a variable into a Boolean. If the variable has content, it will become True. If it's empty or 0, it'll become False. 
#Convert these variables into booleans, and check the output. 

member = "Sam"
middle_name = ""
foot_size = 8.5
sibilings = 0

boolean_member = bool(member)
boolean_middle_name = bool(middle_name)
boolean_foot_size = bool(foot_size)
boolean_sibilings = bool(sibilings)

print(boolean_member)
print(boolean_middle_name)
print(boolean_foot_size)
print(boolean_sibilings)