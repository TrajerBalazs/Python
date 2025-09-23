#-------------------------------------------------------------------------------------------------------------------

#Összehasonlításokkal ellenőrizhetjük, hogy egy karakterlánc egyenlő-e egy másik karakterlánccal vagy sem.

#We can use comparisons to check if a string is equal to or not equal to another string.

print("online" == "online")
print("online" != "offline")

#-------------------------------------------------------------------------------------------------------------------

#Annak ellenőrzésére, hogy egy karakterlánc egyenlő-e egy másik karakterlánccal, egyenlőségoperátort (==) is használunk.
#Ha a bal oldali karakterlánc egyenlő a jobb oldali karakterlánccal, mivel "alma" == "alma", az eredmény Igaz

#To check if a string is equal to another string, we also use equality operator (==).
#If the string on the left is equal to the string on the right, as "apple" == "apple", the result is True

print("apple" == "apple")

#-------------------------------------------------------------------------------------------------------------------

#Ha a bal oldali karakterlánc nem egyenlő a jobb oldali karakterlánccal, például "alma" == "narancs", az eredmény Hamis

#If the string on the left isn't equal to the string on the right, as in "apple" == "orange", the result is False

print("apple" == "orange") 

#-------------------------------------------------------------------------------------------------------------------

#Összehasonlíthatjuk a karakterláncokat tároló változókat egymással is, például a következőben: fruit_1 == fruit_2

#We can also compare variables that store strings with each other, like in fruit_1 == fruit_2

fruit_1 = "apple"
fruit_2 = "orange"
print(fruit_1 == fruit_2)

#-------------------------------------------------------------------------------------------------------------------

#Annak ellenőrzésére, hogy egy karakterlánc egyenlő-e egy másik karakterlánccal, az egyenlőtlenségi operátort használjuk (!=).
#Ha a bal oldali karakterlánc nem egyenlő a jobb oldali karakterlánccal, például "subscribe" != "rejected" esetén, az eredmény Igaz

#To check if a string isn't equal to another string, we use the inequality operator, (!=).
#If the left string isn't equal to the right string, as in "subscribe" != "rejected", the result is True

print("subscribe" != "rejected")

#-------------------------------------------------------------------------------------------------------------------

#Ha a bal oldali karakterlánc megegyezik a jobb oldali karakterlánccal, például a "subscribe" != "subscribe" esetén, az eredmény Hamis.

#If the string on the left is equal to the string on the right, as in "subscribe" != "subscribe", the result is False.

print("subscribe" != "subscribe")

#-------------------------------------------------------------------------------------------------------------------

#Egy összehasonlítás eredményének változóban való tárolásához az = jelet használjuk.

#To store the result of a comparison in a variable, we use = sign. 

same = "subscribe" != "subscribe"
print(same)

#-------------------------------------------------------------------------------------------------------------------