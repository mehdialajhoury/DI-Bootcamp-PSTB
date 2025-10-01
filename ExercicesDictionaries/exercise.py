books = {
    '1984': 'George Orwell',
    'Brave New World': 'Aldous Huxley',
    'The Great Gatsby': 'F. Scott Fitzgerald'
}

#1. Print the author of "1984".

print(books.get("1984"))

#2. Change the author of "The Great Gatsby" to "Francis Scott Fitzgerald".

change = {'The Great Gatsby' : 'F.Scott Fitzgerald'}
books.update(change)
print(books)

#3. Add a new book: "Moby Dick" by Herman Melville.

new_book = {'Moby Dick' : 'Herman Melville'}
books.update(new_book)
print(books)

#4. Use the get() method to try to access the author of "To Kill a Mockingbird".

print(books.get("To Kill a Mockingbird"))

#5. Remove the book "Brave New World" using the pop() method.

books.pop("Brave New World")
print(books)