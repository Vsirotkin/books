from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTestCase(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
    
    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
