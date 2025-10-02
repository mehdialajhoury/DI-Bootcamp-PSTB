#Write a function repeat_word that takes a word and a number as parameters and prints the word that many times.

def repeat_word(word, number : int):
    i=0
    for i in range(number):
        print(word)


repeat_word("hello",5)