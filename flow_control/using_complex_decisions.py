#------------------------------------------------------------------------------------------------------------------------------------------
#We know how to run or skip code based on a condition like age > 16

age = 17
has_permit = True

if age > 16:
    print("Can drive")

#------------------------------------------------------------------------------------------------------------------------------------------


#What if we wanted to run or skip code depending two conditions? Like age > 16 and then has_permit
#The and operator allows us to run code only if both conditions age > 16 and has_permit are True.

age = 17
has_permit = True

if age > 16 and has_permit:
    print("Can drive")

#------------------------------------------------------------------------------------------------------------------------------------------


#The and operator skips the code block if one or more conditions are False, like age > 18.

age = 17
has_permit = True
if age > 18 and has_permit:
    print("Can drive")

#------------------------------------------------------------------------------------------------------------------------------------------


#We can add as many conditions as we want, like here, where we can add another and, and then is_insured to complete the condition.

age = 17
has_permit = True
is_insured = True

if age > 16 and has_permit and is_insured:
    print("Can drive")
#------------------------------------------------------------------------------------------------------------------------------------------

#Some more code:

year = 2000

if year > 1900 and year < 2020:
    print("Valid entry")

#------------------------------------------------------------------------------------------------------------------------------------------

subway_defect = True
is_sunny = True
distance = 2

if subway_defect and is_sunny and distance <= 2:
    print("Walk to work")

#------------------------------------------------------------------------------------------------------------------------------------------

#To run code when either one of the conditions is True, we use the or operator.

avarage_grade = "A"
final_score = 1400

if avarage_grade == "A" or final_score >= 1300:
    print("Certificate achived! ")

#------------------------------------------------------------------------------------------------------------------------------------------


#With or code gets skipped only if all conditions are False, like avarage_grade == "A" and final_score >= 1500

avarage_grade = "B"
final_score = 1400

if avarage_grade == "A" or final_score >= 1500:
    print("Certificate achived!")

#------------------------------------------------------------------------------------------------------------------------------------------

#Here final_score >= 1500 is False, but the code still runs because avarage_grade == "A" is True.

avarage_grade = "A"
final_score = 1400

if avarage_grade == "A" or final_score >= 1500:
    print("Certificate achived!")

#------------------------------------------------------------------------------------------------------------------------------------------

#We can use or to add as many conditions as we want like also adding won_competition.

avarage_grade = "B"
final_score = 1400
won_competition = True

if avarage_grade == "A" or final_score >= 1500 or won_competition:
    print("Certificate achived!")

#------------------------------------------------------------------------------------------------------------------------------------------

#More practice code:

is_weekend = False
on_vacation = True

if is_weekend or on_vacation:
    print("Go on a roadtrip!")

#------------------------------------------------------------------------------------------------------------------------------------------

mobile_internet = False
wifi = False

if mobile_internet or wifi:
    print("Loading inbox ... ")


#------------------------------------------------------------------------------------------------------------------------------------------

highest_score = 100
score = 70
level = 5

if score > highest_score or level == 5:
    print("You won!")

#------------------------------------------------------------------------------------------------------------------------------------------

promote_article = False
views = 100
shares = 30
likes = 70

if views > 150 or shares >= 50 or likes >= 60:
    promote_article = True

print(promote_article)