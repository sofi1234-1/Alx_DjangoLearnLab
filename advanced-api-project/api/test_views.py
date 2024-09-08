# api/test_views.py
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2023-01-01'
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        response = self.client.post(reverse('book-list'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # One existing book + one created book
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Test Book')

    def test_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only the initial book should be returned

    def test_update_book(self):
        update_data = {'title': 'Updated Book'}
        response = self.client.put(reverse('book-detail', args=[self.book.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        response = self.client.get(reverse('book-list') + '?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(reverse('book-list') + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_books(self):
        Book.objects.create(title='Another Book', author='Another Author', published_date='2022-01-01')
        response = self.client.get(reverse('book-list') + '?ordering=published_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Another Book')  # Check if ordered correctly

    def test_permission_denied_on_unauthenticated_user(self):
        self.client.logout()
        response = self.client.post(reverse('book-list'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

