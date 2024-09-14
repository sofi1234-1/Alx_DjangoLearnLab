ExampleForm
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN Number'}),
        }

    def clean_isbn(self):
        """Custom validation for ISBN."""
        isbn = self.cleaned_data.get('isbn')
        if not isbn:
            raise forms.ValidationError('ISBN is required.')
        if len(isbn) != 13:
            raise forms.ValidationError('ISBN must be exactly 13 digits.')
        # Add more validation as needed
        return isbn

    def clean_title(self):
        """Custom validation for Title."""
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Title cannot be empty.')
        return title

    def clean(self):
        """General validation."""
        cleaned_data = super().clean()
