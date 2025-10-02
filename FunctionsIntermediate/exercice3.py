#Write a function count_to_number that takes a number as a parameter and prints all numbers from 1 to that number.

def count_to_number(number : int):
    for i in range(1,number+1,1):
        print(i)

count_to_number(7)