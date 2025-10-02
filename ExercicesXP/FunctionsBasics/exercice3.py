#Write a function check_even_odd that takes one number and prints “Even” if the number is even, and “Odd” if the number is odd.

def check_even_odd(number : int):
    if number % 2 == 0:
        return("Even")
    else:
        return("Odd")
    
print(check_even_odd(28))