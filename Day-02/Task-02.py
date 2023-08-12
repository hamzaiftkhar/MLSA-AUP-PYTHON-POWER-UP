"""Question-2: 
Nested Dictionaries You are managing a library. Here's the information about some books:

books = { 'book1': { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925 }, 'book2': { 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960 }, 'book3': { 'title': '1984', 'author': 'George Orwell', 'year': 1949 } } 

a) Add a new book to the dictionary with the title, author, and year. 
b) Print the titles of all the books. 
c) Determine the book with the earliest publication year and print its title and author."""

# Answer-2:

# a) Add a new book to the dictionary with the title, author, and year.
books = {'book1': {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},'book2': {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960}, 'book3': {'title': '1984', 'author': 'George Orwell', 'year': 1949}}

books['book4'] = {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'year': 1988}

# b) Print the titles of all the books.
for i in books:
    print(books[i]['title'])

# c) Determine the book with the earliest publication year and print its title and author.
min_year = min(books[i]['year'] for i in books)
for i in books:
    if books[i]['year'] == min_year:
        print("The book with the earliest publication year is: ", books[i]['title'], "by", books[i]['author'])
        
