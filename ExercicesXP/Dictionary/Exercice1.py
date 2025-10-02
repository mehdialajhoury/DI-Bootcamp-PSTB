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

