from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

# Example usage:
if __name__ == "__main__":
    # Example: Find books by "George Orwell"
    orwell_books = query_books_by_author("George Orwell")
    print("Books by George Orwell:")
    for book in orwell_books:
        print(book)

    # Example: Find books in "Central Library"
    central_library_books = query_books_in_library("Central Library")
    print("nBooks in Central Library:")
    for book in central_library_books:
        print(book)

    # Example: Find librarian for "Central Library"
    central_library_librarian = query_librarian_for_library("Central Library")
    print("nLibrarian for Central Library:")
    print(central_library_librarian)
