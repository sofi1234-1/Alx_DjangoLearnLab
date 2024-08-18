from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)  # Create a Book instance
book.save()  # Save the book to the database
# Expected Output:  None (indicating successful save)
   