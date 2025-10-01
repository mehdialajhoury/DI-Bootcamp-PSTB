list = [1, 2, 3, 4]

#Given a list [1, 2, 3, 4], print out all the values in the list one by one.
for i in list:
    print(i)

#Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.
for i in list:
    print(i*20)

#Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].
list = ["Elie", "Tim", "Matt"]
new_list = []
for i in list:
    new_list.append((i[0]))
print(new_list)

#Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].
list = [1, 2, 3, 4, 5, 6]
new_list = []
for i in list:
    #Si l'élément de la liste est pair, on l'ajoute à la nouvelle liste
    if (i % 2) == 0:
        new_list.append(i)
print(new_list)

#Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
new_list = []

for i in list1:
    for j in list2:
        if i == j:
            new_list.append(i)
print(new_list)

#Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].
list = ["Elie", "Tim", "Matt"]

new_list = []
for i in list:
    i.lower()
    new_list.append(i.lower()[::-1])
print(new_list)

#Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].
first="first"
third="third"

new_list = []

for i in first:
    for j in third:
        if i == j:
            new_list.append(i)
print(new_list)

#For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].

new_list = []

for i in range(1,100,1):
    if (i % 12) == 0:
        new_list.append(i)
print(new_list)

#Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].

string="amazing"
vowels = ["a", "e", "i", "o", "u"]
list = []

for i in string:
    if i not in vowels:
        list.append(i)
print(list)

#Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

list = []
final_list = []
for i in range(3):
    list.append(i)
    for j in range(1):
        final_list.append(list)
print(final_list)

#Generate a list with the following structure:

#[
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#]

list = []
final_list = []
for i in range(10):
    list.append(i)
    for j in range(1):
        final_list.append(list)
print(final_list)