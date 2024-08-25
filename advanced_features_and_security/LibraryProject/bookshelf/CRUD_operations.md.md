# CRUD Operations for Book Model
## Create
python
>>> from bookshelf.models import Book
>>> book = Book(title="1984", author="George Orwell", publication_year=1949)  # Create a Book instance
>>> book.save()  # Save the book to the database
>>> # Expected Output:  None (indicating successful save)
## Retrieve
python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984") 
>>> print(book.title, book.author, book.publication_year)
>>> # Expected Output: 1984 George Orwell 1949
## Update
python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
>>> # Expected Output: Nineteen Eighty-Four
## Delete
python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
>>> Book.objects.all()
>>> # Expected Output: <QuerySet []> (empty queryset)
