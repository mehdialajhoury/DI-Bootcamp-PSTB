#Write a program that will calculate cat’s and dog’s years based on human years:

#I have a cat and a dog. I got them at the same time as kitten/puppy. That was humanYears years ago. Print their respective ages now as [humanYears,catYears,dogYears]

#NOTES:

#humanYears >= 1 humanYears are whole numbers only

#Cat Years 15 cat years for first year +9 cat years for second year +4 cat years for each year after that

#Dog Years 15 dog years for first year +9 dog years for second year +5 dog years for each year after that

human_age=int(input("Quel est l'age de l'humain ?"))

if human_age == 0:
    cat_age=0
    dog_age=0
elif human_age ==1:
    cat_age=15
    dog_age=15
elif human_age ==2:
    cat_age=15+9
    dog_age=15+9
elif human_age > 2:
    cat_age=15+9
    dog_age=15+9
    for i in range(3,human_age+1):
        cat_age=cat_age+4
        dog_age=dog_age+5

ages = [human_age, cat_age, dog_age]

print(ages)
