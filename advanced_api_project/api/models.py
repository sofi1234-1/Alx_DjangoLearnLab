from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# ... code ...
class Author(models.Model):
    """
    Represents an author of a book.
    """
    # ... code ...
class Book(models.Model):
    """
    Represents a book, with a title, publication year, and a foreign key relationship to the Author model.
    """
    # ... code ...
   

   
