#----------------------------------------------------------------------------------------------------------------------------------
#Összehasonlító operátorokat használhatunk olyan programokban, mint a Trivia alkalmazás, hogy ellenőrizzük, helyes-e a válasz egy kérdésre.
#Írjuk be a == karakterláncot ebbe a programba, hogy összehasonlítsuk a kivételes megoldást a megadott válasszal.


#We can use comparison operators in programs like Trivia app to check if the answer to a question is correct. 
#Type == in this program to compare the excepted solution to the given answer.

answer = "Picasso"
if answer == "Picasso":
    print(answer + " is correct!")

#----------------------------------------------------------------------------------------------------------------------------------
#Mi van, ha a kvíz válasza nem helyes? Használhatjuk a != egyenlőtlenségi operátort, hogy ellenőrizzük, a válasz nem egyenlő-e "Picasso"-val.

#What if the trivia quiz answer isn't correct? We can use the inequality operator != to check if answer is not equal to "Picasso".

answer = "Matisse"
if answer != "Picasso":
    print(answer + " is wrong!")

#----------------------------------------------------------------------------------------------------------------------------------
#Az if utasítások az összes eddig tárgyalt összehasonlító operátorral működnek. Például annak ellenőrzése, hogy az életkor nagyobb vagy egyenlő-e 55-tel.

#if statements work with all comparison operators we've explored so far. Like checking if age is greater than or equal to 55.

age = 75
if age >= 55:
    print("Discount applied")

#----------------------------------------------------------------------------------------------------------------------------------
#Vagy a == használatával összehasonlíthatjuk az olyan változókat, mint az is_day, a logikai értékekkel.


#Or using == to compare variables like is_day to boolean values.

is_day = True
if is_day == True:
    print("Lights off!")

#----------------------------------------------------------------------------------------------------------------------------------
#Az összehasonlítás eredményét egy változóban tárolhatjuk. Itt az 50-nél nagyobb pontszámú összehasonlítást a pass_grade változóban tároltuk.
#Használd a pass_grade változót a feltételes módban a Passed! megjelenítéséhez a konzolon.

#We can store the result of a comparison in a variable. Here, we stored the score > 50 comparison in the pass_grade variable.
#Use the pass_grade variable in the conditional to display Passed! in the console.

score = 51
pass_grade = score > 50
if pass_grade:
    print("Passed!")

