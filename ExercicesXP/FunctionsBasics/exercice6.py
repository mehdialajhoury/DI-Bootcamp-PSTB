#Write a function check_sign that takes a number and prints whether the number is positive, negative, or zero.

def check_sign(number : int):
    if number > 0:
        print("Positive")
    elif number <0:
        print("Negative")
    elif number == 0:
        print("Zero")

check_sign(-5)
check_sign(10)
check_sign(0)