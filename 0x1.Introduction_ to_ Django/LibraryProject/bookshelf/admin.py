from django.contrib import admin
from .models import Book

admin.site.register(Book)
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author__name')  # Use double underscores for related fields

admin.site.register(Book, BookAdmin)
