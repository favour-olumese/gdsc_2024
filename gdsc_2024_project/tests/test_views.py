from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import Permission, Group
from django.contrib.auth import get_user_model
User = get_user_model()

class BookViewsTest(TestCase):
    def setUp(self):
        david = User.objects.create_user(username='david', password='defeatgoliath')
        david.save()

    def test_book_list_view_url_exists_at_desired_location(self):
        login = self.client.login(username='david', password='defeatgoliath')
        response = self.client.get('/books/')        
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_url_redirects_when_not_logged_in(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/books/')

    def test_book_list_view_url_accessible_by_name(self):
        login = self.client.login(username='david', password='defeatgoliath')
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_uses_correct_template(self):
        login = self.client.login(username='david', password='defeatgoliath')
        response = self.client.get(reverse('book-list'))
        self.assertTemplateUsed(response, 'gdsc_2024_project/book_list.html')

    
class AdminPageTest(TestCase):
    def setUp(self):
        david = User.objects.create_user(username='david', password='defeatgoliath')
        david.save()

        admin = User.objects.create_superuser('admin', 'admin@example.com', 'iamthebosshere')
        admin.save()

    def test_admin_page_is_only_accessible_by_admin(self):
        login = self.client.login(username='david', password='defeatgoliath')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        login = self.client.login(username='admin', password='iamthebosshere')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)