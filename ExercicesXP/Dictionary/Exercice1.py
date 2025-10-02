import string
#1. Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).

list = [("name", "Elie"), ("job", "Instructor")]
dictionary = {}

for i in list:
    dictionary[i[0]] = i[1]
print(dictionary)

#2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
dictionary = {}

for i in list1:
    for j in list2:
        #J'utilise les index de chaque liste, pour savoir si j'ajoute au dictionnaire un élément : si l'index est le même
        #J'ajoute à mon dictionnaire comme 1ère paire de clé/valeur CA : California, et ainsi de suite
        if list1.index(i) == list2.index(j):
            dictionary[i] = j
print (dictionary)

#3. Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).

vowels = ["a", "e", "i", "o", "u"]
dictionary = {}

for i in vowels:
    dictionary[i] = 0
print(dictionary)

#4. Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. You should return something like this:

#Utilisation de la bibliothèque String, fonction ascii_uppercase, qui retourne la liste des lettres de l'alphabet en majuscule
alphabet = string.ascii_uppercase
dictionary = {}

for i in alphabet:
    dictionary[alphabet.index(i)+1]=i
print(dictionary)

#Super Bonus: Given the string "awesome sauce", return a dictionary where the keys are vowels, and the values are the count of each vowel in the string. Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.

string = "awesome sauce"
vowels = ["a", "e", "i", "o", "u"]
dictionary = {}
new_string = ""

#Utilisation d'une string additionnelle pour ne stocker qu'uniquement les voyelles totales présentes dans la string initale

for i in string:
    if i in vowels:
        new_string = new_string + i
print(new_string)

# Parcours de la string additionnelle et comptage de chaque élément dedans puis association de chaque élément et de son occurence dans un dictionnaire
for i in new_string:
    print(i)
    print(new_string.count(i))
    dictionary[i] = new_string.count(i)
print(dictionary)