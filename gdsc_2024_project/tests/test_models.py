from django.test import TestCase
from gdsc_2024_project.models import Book


from django.contrib.auth import get_user_model
User = get_user_model()


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Set up non-modified objects used by all test methods
        Book.objects.create(author='Respectable Sins', book_name='Jerry Bridges', publisher='NavPress Publishing Group')

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label , 'author')

    def test_author_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author').max_length
        self.assertEqual(max_length , 150)

    def test_book_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('book_name').verbose_name
        self.assertEqual(field_label , 'book name')

    def test_book_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('book_name').max_length
        self.assertEqual(max_length , 200)

    def test_publisher_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('publisher').verbose_name
        self.assertEqual(field_label , 'publisher')

    def test_publisher_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('publisher').max_length
        self.assertEqual(max_length , 350)

    def test_object_name_is_book_name(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.book_name
        self.assertEqual(expected_object_name, str(book))

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/books/')