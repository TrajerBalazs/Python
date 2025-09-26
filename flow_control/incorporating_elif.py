#----------------------------------------------------------------------------------------------------------------------------------
#Tanuljuk meg, hogyan írjunk feltételes utasításokat, amelyek adott feltételeket kezelnek.
#Az if és az else utasítások használatával írhatunk egy olyan programot, amely egy üdvözlő szöveget jelenít meg,
# ha az óra kisebb, mint 12, és egy másikat, ha nem teljesíti a feltételt.

#Let's learn how to write conditional statements that handle specific conditions.
#Using if and else statements, we can write a program that shows one greeting if hour is less than 12 and another if it does not fulfill the condition.

hour = 9
if hour < 12:
    print("Good morning")
else:
    print("Good night")

#----------------------------------------------------------------------------------------------------------------------------------
#Egy konkrétabb feltételhez, például ha az óra nagyobb, mint 12, de kisebb, mint 17, az elif óra < 17 kódot használhatjuk.
# Az elif az else if rövidítése. Az elif utasítást akkor használjuk, ha van egy második feltétel, amelyet ellenőrizni kell, amikor az if blokk feltétele nem teljesült.
# Az elif utasítás lefuttatja a kódblokkját, ha az előző if feltételek hamisak voltak, és a feltétele, például az óra < 17, igaz.

#For a more specific condition, like if hour is greater than 12, but less than 17, we can code elif hour < 17 : instead.
# elif stands for else if. elif is used when there is a second condition to be checked when the condition of the if block was not met.
#The elif statement runs its code block if the conditions before if were False and its condition, like hour < 17 is True.

hour = 14
if hour < 12:
    print("Good morning")
elif hour < 17 :
    print("Good afternoon")

#----------------------------------------------------------------------------------------------------------------------------------
#Kódolhatunk egy else utasítást úgy, hogy a kódblokkja akkor fusson le, amikor az if és elif feltételek hamisak.

#We can code an else statement to run its code block when the if and elif conditions are False.

hour = 18
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
else:
    print("Good night")

#----------------------------------------------------------------------------------------------------------------------------------
#Amíg az else utasítás elé kerülnek, annyi elif utasítást adhatunk hozzá, amennyit csak szeretnénk.

#As long as they go before the else statement, we can add as many elif statement as we'd like.

hour = 20
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
elif hour < 21:
    print("Good evening")
else :
    print("Good night.")