#1. Asks the user to input a sentence.
sentence = input("Ecrivez une phrase")

#2. Checks if the sentence is made up of only alphabetic characters. If not, print how many non-alphabetic characters are in the sentence.

print(sentence.isalpha())

counter=0

if sentence.isalpha() is False:
    for i in sentence:
        if i.isalpha() is False:
            counter=counter+1
print("Il y a", counter, "caractères non alphabétique dans votre phrase")

#3. Determines if the sentence ends with an exclamation mark (!).

if sentence.endswith("!"):
    print("Votre phrase contient un point d'exclamation à la fin")
else:
    print("Votre phrase ne contient pas de point d'exclamation à la fin")

#4. Finds out if the sentence contains any whitespace characters and prints a message accordingly.

for i in sentence:
        if i.isspace() is True:
             print("Il y a au moins un espace dans votre phrase")