#----------------------------------------------------------------------------------------------------------------------------------
#Az okos programok logikai értékeket használnak annak eldöntésére, hogy lefussanak-e a kódsorok, vagy kihagyják-e őket.

#Ha utasítást használunk olyan kód írásához, amely különböző helyzetekre reagál. Ezt az if kulcsszóról ismerjük fel.
#Az if utasítás csak akkor futtatja a kódot, ha igaznak értékelődik ki. Ez olyan, mintha azt mondanánk, hogy ha valami igaz, akkor tedd ezt.
#Tegyük a kiértékelést igazra egyszerűen a True logikai érték használatával, hogy a "Hello" szöveg jelenjen meg a konzolon.

#Smart programs use booleans to make decisions on whether to run lines of code or skip them.

#We use an if statement to write code that responds to different situations. We recognize it by the keyword if.
#The if statement runs code only if it is evaulated as true. It's like saying, if something is true, than do this.
#Let's make the evaluation true by simply using the boolean value True to display "Hello" in the console.

if True:
    print("Hello!")

#----------------------------------------------------------------------------------------------------------------------------------
#De mit akarunk kihagyni a kódból? Ebben az esetben a kiértékeléshez hamisra van szükségünk.
#Tegyük egyszerűen hamisra értékelhetővé a kiértékelést a Hamis logikai érték használatával. Semmi sem fog kiírni.

#But what is we want to skip the code? In that case, we need the statement to evaluated as false.
#Let's easily make the statement evaluable to false by simply using boolean value False. Nothing will print.

if False:
    print("Hello")

#----------------------------------------------------------------------------------------------------------------------------------
#Az olyan értékeket, mint az Igaz, feltételeknek nevezzük. A feltételekre támaszkodó utasításokat feltételes utasításoknak nevezzük. 
#A feltételek döntik el, hogy a kód lefut-e vagy kimarad. Az „ha” és a kettőspont között helyezkednek el: .

#Values like True are called conditions. Statements relying on conditions are called conditionals. 
#Conditions decide if the code runs or gets skipped. They come in between if and the colon : . 

if True:
    print("Hello")

#----------------------------------------------------------------------------------------------------------------------------------
#Az if utasítás nem dönt a kód kihagyásáról vagy a teljes kód futtatásáról. Csak egy kódblokkról hoz döntéseket.

#if statement don't decide on skipping or running the entire code. They only make decisions about a code block. 

if True:
    print("I'm a code block!")

#----------------------------------------------------------------------------------------------------------------------------------
#Két szóköznyi behúzást használunk a kódblokkok kiemelésére, például ennek a megjelenítési utasításnak a behúzása esetén. 
#A behúzás a kód és a kódszerkesztő margója közötti távolságra utal.

#We use an indentation of two spaces to higlight code blocks, like indenting this display statement. 
#Indentation refers to the space between the code and the code editor's margin. 
if True:
    print("I'm two space away!")

#----------------------------------------------------------------------------------------------------------------------------------
#Egy kódblokk lehet több, mint egy egysoros. Minden azonos behúzású sor ugyanahhoz a kódblokkhoz tartozik.
#Itt láthatjuk, amikor a print() függvénnyel egy újabb sort adunk hozzá az elejéhez.

#A code block can be more than a one-liner. All lines with the same indentation belong to the same code block.
#We can see it here when we use print() to add one more line at the beginning.

if True:
    print("Look at me!")
    print("I'm a code block")

#----------------------------------------------------------------------------------------------------------------------------------
#Ha a behúzás helytelen, a számítógép nem érti a kódodat. Ez egy IndentationError hibaüzenetet eredményez a konzolon.
# Itt a második print() hibásan csak egy szóközzel van behúzva kettő helyett, mint az első print().

#If the indentation is incorrect, the computer can't understand your code. This leads to an IndentationError showing up in the console.
# Here, the second print () is wrongly indented by only one space instead of two, like the first print().

#if True:
#   print("Look at me!")
#  print("I'm a code block")

#----------------------------------------------------------------------------------------------------------------------------------
#A logikai True érték használata helyett elmenthetjük egy változóba, például a great-be, és feltételként használhatjuk.

#Instead of using a boolean True, we can save it in a variable like great and use it as the condition.

greet = True
if greet:
    print("Hello")

#----------------------------------------------------------------------------------------------------------------------------------
#Egy olyan változó, mint a greet, hamis értékre állításával kihagyhatjuk a kódot, például a display utasítást.

#Using a variable like greet set to False allows us to skip code like the display statement.

greet = False
if greet:
    print("Hello!")