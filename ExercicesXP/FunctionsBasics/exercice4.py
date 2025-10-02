#Write a function sum_list that takes a list of numbers as a parameter and returns the sum of all numbers in the list.

list_numbers = [2,4,5,6,9]

def sum_list(numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return (sum)

print(sum_list(list_numbers))