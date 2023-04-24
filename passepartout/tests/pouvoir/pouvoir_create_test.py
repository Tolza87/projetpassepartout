from django.test import TestCase
from django.urls import reverse

class PouvoirCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_pouvoir_create_page(self):
        response = self.client.get(reverse('pouvoir_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pouvoir/pouvoir_create.html')