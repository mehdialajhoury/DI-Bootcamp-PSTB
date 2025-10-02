#1. Write a function greet_person that takes two parameters: name (string) and age (integer). The function should return a message that says:

#"Hello, [name]! You are [age] years old."
#2. Modify the function greet_person to accept a default age of 25 if no age is provided.

#Example Outputs:
#For greet_person("Alice", 30), the output should be: "Hello, Alice! You are 30 years old."
#For greet_person("Bob"), the output should be: "Hello, Bob! You are 25 years old."

def greet_personn(name,age=25):
    return f"Hello, {name} ! You are {age} years old"

print(greet_personn("Mehdi"))