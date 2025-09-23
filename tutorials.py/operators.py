#-------------------------------------------------------------------------------------------------------------------

#Ellenőrizhetjük, hogy egy szám kisebb-e egy másiknál, ehhez a kisebb-mint operátort használjuk. <
#Ha a bal oldali szám kisebb, mint a jobb oldali, az eredmény Igaz.

#We can check if a number is less then another number, we use the less-than operator. <
#If the number on the left is less than the number on the right, the result is True.

print(1 < 90)

#-------------------------------------------------------------------------------------------------------------------

#De ha a bal oldali szám nem kisebb, mint a jobb oldali szám, akkor az eredmény hamis.

#But if the number on the left is isn't less then the number on the right, the result is False.

print(235 < 1)

#-------------------------------------------------------------------------------------------------------------------

#Az ellentét ellenőrzéséhez használhatunk egy nagyobb-mint-operátort. >
#És ha a bal oldali szám nagyobb, mint a jobb oldali, akkor az eredmény Igaz.

#To check the oposite we can use a greater-then operator. >
#And if the number on the left is grater than the number on the right, the result is True. 

print(101 > 90)

#-------------------------------------------------------------------------------------------------------------------

#De ha a bal oldali szám nem nagyobb, mint a jobb oldali, akkor az eredmény hamis.

#But if the number on the left is isn't grater then the number on the right, the result is False.

print(1 > 235)

#-------------------------------------------------------------------------------------------------------------------

#És ha balra és jobbra ugyanazt a számot kapjuk, az eredmény hamis, mert egyenlőek.

#And if we get a same number on the left and right, the result is False, because they equal.

print(5 < 5)
print(5 > 5)

#-------------------------------------------------------------------------------------------------------------------

#Annak ellenőrzésére, hogy egy szám kisebb vagy egyenlő-e egy másik számmal, a kisebb-vagy-egyenlő-val/-vel operátort használjuk. <=

#To check if a number is less than or equal to another number we use the less-than-or-equal-to operator. <=

print(1 <= 3)
print(11 <= 11)

#-------------------------------------------------------------------------------------------------------------------

#Annak ellenőrzésére, hogy egy szám nagyobb vagy egyenlő-e egy másik számmal, a nagyobb vagy egyenlő operátort használjuk. >=

#To check if a number is grater than or equal to another number, we use the greater-than-or-equal-to operator. >=

print(300 >= 200)
print(300 >= 300)

#-------------------------------------------------------------------------------------------------------------------

#Egy összehasonlítás eredményének változóban való tárolásához az = jelet használjuk.

#To store a result of a comparison in a variable, we use the = sign. 

result = 1 <= 100
print(result)

#-------------------------------------------------------------------------------------------------------------------

#Használhatunk összehasonlító operátort is egy változó egy másik változóval való összehasonlítására, például a (min <= max) képletben.

#We can also use a comparison operator to compare a variable with another variable, like in (min <= max).

min = 5
max = 10
result = min <= max
print(result)

battery_level = 10
low = battery_level <= 20
print("Low battery!")
print(low)

#-------------------------------------------------------------------------------------------------------------------