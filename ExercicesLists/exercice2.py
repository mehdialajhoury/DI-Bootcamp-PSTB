fruits = ["apple", "banana", "cherry", "date", "elderberry"]

#1. Add "fig" to the end of the fruits
fruits.append("fig")
print(fruits)

#2. Insert "grape" at the beginning of the list
fruits.insert(0,"grape")
print(fruits)

#3. Remove "cherry" from the list using using the specific method for it
fruits.remove("cherry")
print(fruits)

#4. Remove the last element from the list using the specific method for it
fruits.pop()
print(fruits)

#5. Create another list of berries and combine it with the fruits list into a list called "combined_list"

berries = ["groseille", "myrtille", "mûre"]
fruits.extend(berries)
print(fruits)

#6. Sort the combined_list
fruits.sort()
print(fruits)

#7. Slice the last three elements of the combined list
print(fruits[-3:])