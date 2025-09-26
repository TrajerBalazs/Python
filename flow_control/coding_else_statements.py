#----------------------------------------------------------------------------------------------------------------------------------
#Egy jó szoftver nem csak eldönti, hogy mit tegyen, ha egy feltétel igaz, hanem tartalék terve is van arra az esetre, ha a feltétel hamis.
#Már tudjuk, hogy az utasítások segítenek-e a kód végrehajtásában, ha egy feltétel, például az avaliable igaz.

#Great software doesn't just decide what to do when a condition is True, it also has a back-up plan if the condition is False.
#We already know if statements help us execute code if a condition like avaliable is True.

available = True
if available:
    print("In stock")

#----------------------------------------------------------------------------------------------------------------------------------
#Adjunk hozzá egy másik if utasítást, amely a not operátort használja egy másik kódblokk futtatásához, ha a feltétel hamis. 
#Írjunk egy not-ot az available elé.

#Let's add another if statement that uses the not operator to run a different code block if the condition is False. 
#Code not avaliable.

available = True

if available:
    print("In stock")
if not available:
    print("Out of stock")

#----------------------------------------------------------------------------------------------------------------------------------
#Két if utasítás létrehozása helyett egy if/else utasítást használunk ugyanazon eredmény eléréséhez.
#Az in/else utasítás else utasítása mindig a végére kerül.

#Instead of creating two if statements, we use an if/else statement to achive the same result.
#The else statement of an in/else statement always goes at the end.

available = False

if available :
    print("1 in stock")
else:
    print("Out of stock")

#----------------------------------------------------------------------------------------------------------------------------------
#Nézzünk meg egy használati esetet: ha az is_day értéke True, akkor le szeretnénk kapcsolni a villanyt.

#Let's look at a use case: if is_day is True, we want to turn the lights off.

is_day = True
if is_day:
    print("Lights off!")

#----------------------------------------------------------------------------------------------------------------------------------
#Ha az is_day értéke hamis, akkor az else utasításban található kód kapcsolja fel a lámpát.

#If is_day is False, the code in the else statement switches the light on.

is_day = False

if is_day:
    print("Lights off!")
else:
    print("Lights on!")

#----------------------------------------------------------------------------------------------------------------------------------
#Az else utasításnak nincs szüksége saját feltételre. Ez azért van, mert kezeli azokat az eseteket, amikor az if feltétele hamis.
#Az else utasítás egy alapértelmezett válaszként működik. Itt az összes 1-től eltérő szám esetén az „It's not 1” üzenetet kell megjelenítenie.

#The else statement doesn't need its own condition. That's because it handles the cases where the if's condition is False.
#The else statement is like a default response. Here, it should display "It's not 1" for all numbers not equal to 1.

number = 99

if number == 1:
    print("It's 1")
else:
    print("It's not 1")

