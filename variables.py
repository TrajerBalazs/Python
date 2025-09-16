#A változóknak mindig kell egy név. Nem lehet nagybetű, és nem lehet szóköz a szavak között. A tökéletes név: változó_neve (Mindent tartalmaz a változónkról.)
#Minden alkalommal, amikor létrehozunk egy változót, értéket kell adnunk neki. Ebben a gyakorlatban John értéket adunk a változónak.

#Variables always need a name. It can't be capital letter and can't be a space between the words. Perfect name: variable_name (It contains everything about our variable.)
#Everytime when we make a variable we need to give them value. In this practice we  give John value to the variable.
variable_name = "John"
#---------------------------------------------------------------------------------------------------------------------------------------


#Ha szeretnénk, számot is adhatunk a változó nevének.

#If we want we can give a number to a variable name.
variable_name2 = "David"
#---------------------------------------------------------------------------------------------------------------------------------------


#Az utasítások sorrendje azért fontos, mert a számítógép sorról sorra követi azokat.

#The order of instructions matter because the computer follows the instructions line by line. 
step_one = "Print this in "
step_two = "the console!"
#---------------------------------------------------------------------------------------------------------------------------------------


#Aztán látjuk a konzolt, amikor látjuk a kimeneteinket.

#Then we see the console when we see our outputs. 

print(step_one + step_two)
#---------------------------------------------------------------------------------------------------------------------------------------


#A változókat azért nevezzük változóknak, mert az általuk tárolt értékek változhatnak. Ahogy mondtam, a számítógép sorról sorra olvassa a kódot,
# és ha ugyanazt a változót más értékkel adjuk hozzá, a számítógép a frissített értéket fogja mutatni.

#Variables are called variables because the values they store can change. As i said, the computer read the code line by line and if we add a same variable with a different
#value the computer will show the updated one. 
variable_name = "John"

print(variable_name)

variable_name= "John"
variable_name = "Peter"

print(variable_name)
#---------------------------------------------------------------------------------------------------------------------------------------


#A változók számértékeket is tárolhatnak.
#Tárolhatunk egy változót, és elvégezhetünk néhány műveletet a változón belül.
#És ha akarjuk, elvégezhetünk néhány műveletet a változóban vagy a nyomtatási sorban.

#Variables can store number values too.
#We can store a variable and do some operations inside a variable.
#And if we want, we can do some operations in the variable or the print line. 


variable_age = 10 + 4
variable_number = 4 / 2
variable_operate = variable_age - 5

print(variable_operate * variable_number)
#---------------------------------------------------------------------------------------------------------------------------------------


#Az utolsó változó speciális értékeket tárolhat. Ez se nem karakterlánc, se nem szám. Nincsenek idézőjelek körülötte, és nem numerikus érték.
#Ez egy logikai érték (Igaz vagy Hamis)

#Last one variables can store a special values. That's neither a string or a number. There are no quotes around it, and it's not a numerical value. 
#That's a bool value (True or False)

variable_bool = True

print(variable_bool)
#---------------------------------------------------------------------------------------------------------------------------------------


#A „not” kód, ami az „Igaz” kifejezés elé áll, „Hamis” eredményt ad. A „not” egy tagadó operátor, ami az értékeket az ellenttéjükké alakítja.

#The code not in front of True makes the expression result in False. not is a negation operator and it turns values into their opposite.
variable_bool = True
print(not variable_bool)
#---------------------------------------------------------------------------------------------------------------------------------------


#Láttuk, hogyan lehet értékeket létrehozni és tárolni, de összehasonlíthatjuk őket egymással.
#Az egyenlőség operátorral (==) ellenőrizhetjük, hogy a felhasználó által megadott PIN kód megegyezik-e a mentett PIN kóddal.

#We saw how to create and store values, but we can compare them to each other.
#we can check user's entered PIN matches their saved PIN with equality operator (==). 

entered_pin = 5448
saved_pin = 5440

print(entered_pin == saved_pin)
#---------------------------------------------------------------------------------------------------------------------------------------

#Megtehetjük az ellenkezőjét is, és egy egyenlőtlenség-operátorral (!=) ellenőrizhetjük, hogy nem egyenlőek-e

#We can do the opposite and we can check they isn't equal with an inequality operator (!=)

print(1 != 10)