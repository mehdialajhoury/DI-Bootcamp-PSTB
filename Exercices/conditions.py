# Prompt the user for input
secret_word = input("Guess the secret word: ")

# Check the input and respond accordingly
if secret_word == "Python":
    print("Correct! You guessed the secret word!")
elif secret_word == "Java":
    print("Not quite, but close!")
elif secret_word.isdigit():
    print("Vous avez entré un nombre, réessayez !")
else:
    print("Try again!")