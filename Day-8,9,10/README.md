# Library-Management-System

Library Management System

Assignment Goal: 
Design and implement a Library Management System using Object-Oriented Programming concepts in Python. The system should allow users to interact with books, patrons, and library operations.

Requirements:

1. Create a Book class with the following attributes:
	Title
	Author
	ISBN
	Total number of copies
	Number of available copies

2. Create a "Patron" class with the following attributes:
	Name
	Patron ID
	Books borrowed (a list of book objects)

3. Create a "Library" class that contains:
	- A list of book objects
	- A list of patron objects

4. Implement the following methods for the Library class:
	- add_book(book): Add a book object to the library's list of books.
	- add_patron(patron): Add a patron object to the library's list of patrons.
	- borrow_book(patron, book): Allow a patron to borrow a book. Update the book's available copies accordingly.
	- return_book(patron, book): Allow a patron to return a book. Update the book's available copies accordingly.

5. Ensure the following:
	- Books cannot have negative available copies.
	- Patrons cannot borrow more copies of a book than available.
	- Patrons cannot return a book they didn't borrow.

6. Create a Catalog class that:
	- Has methods to display all books and all patrons in the library.


Challenge Tasks (Optional, for extra complexity):

1. Implement a due date for borrowed books and calculate overdue fines.
2. Create an administrator role that can add/remove books and manage patron records.
3. Implement a reservation system for books that are currently borrowed.
4. Use file I/O to save and load library data.

Create a well-structured Python program that implements the above requirements. Use proper class design, encapsulation, and methods. Comment your code appropriately to explain your logic.
