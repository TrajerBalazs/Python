#Let's learn a new concept which explains how variables keep track of things like adding or removing dollars from wallet.
#When we create a variable, we assign it a value, like assigning 3 to wallet.

wallet = 3

print(wallet)

#Self-assignment is when we set a variable to its own value. For example, we can set wallet to its value 3 with wallet = wallet

wallet = 3 
wallet = wallet
print(wallet)

#Because we can self-assign variables, we can increase or decrease variables set to numbers.

wallet = 3
wallet = wallet + 1

print(wallet)

#Self-assigning variables let us track data that changes over times. For example, a user might add 2 dollars to a wallet and then remove 1.

wallet = 3
wallet = wallet + 2
wallet = wallet - 1
print(wallet)


#Variables set to strings work the same way. Try setting name to name + "John".

name = "Account name: "
name = name + " Elton"
name = name + " John"

print(name)

#We know we can add 1 to a variable by writing out the variable's name. In this case, let's add one to likes.

likes = 5
likes = likes + 1

print(likes)

#Rather than rewriting the variable's name, we can use the += operator to add a number with sales += 1.

sales = 5 
sales += 1

print(sales)

#To subtract from a variable's value, we use -= operator.

sales = 5 
sales -= 3

print(sales)