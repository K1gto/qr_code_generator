from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import QRCode

class QRCodeGeneratorTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.history_url = reverse('history')

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_register_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_user(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_user(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.home_url)

    def test_logout_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)

    def test_generate_qr_code(self):
        self.client.login(username='testuser', password='testpass')
        link = 'https://www.example.com'
        response = self.client.post(self.home_url, {'link': link})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, link)
        self.assertTrue(QRCode.objects.filter(link=link, user=self.user).exists())

    def test_qr_code_history(self):
        self.client.login(username='testuser', password='testpass')
        QRCode.objects.create(link='https://www.example.com', user=self.user)
        response = self.client.get(self.history_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'history.html')
        self.assertContains(response, 'https://www.example.com')
