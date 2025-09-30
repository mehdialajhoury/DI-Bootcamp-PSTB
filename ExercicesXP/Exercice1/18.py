#Check whether a string called my_string is all in lowercase.
my_string = "test"

for i in my_string :
    if i.islower():
        result = True
    else :
        result = False
        break
if result:
    print("la chaîne est toute en minuscule")
else :
    print("la chaine comporte au moins une majuscule")