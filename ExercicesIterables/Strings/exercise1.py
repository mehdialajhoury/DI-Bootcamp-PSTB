text = "Python is Fun!"

#1. Convert the entire string to uppercase
text = text.upper()
print(text)

#2. Make the first letter upper case
text = text.capitalize()
print(text)

#3. Make the first letter of each word upper case
text = text.title()
print(text)

#4. Find the index of "F". What happens if you use lower case in the method?
text = text.find("F")
print(text)

text = "Python is Fun!"
#5.Find a substring
text = text.find("thon")
print(text)