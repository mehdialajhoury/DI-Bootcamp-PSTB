#Ask the user for a number. If the number is negative, show a message that says 
# "That number is less than 0!" If the number is positive, show a message
# that says "That number is greater than 0!" Otherwise, show a message that 
# says "You picked 0!.
number = int(input("Choisis un nombre :"))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else :
    print("You picked 0!")