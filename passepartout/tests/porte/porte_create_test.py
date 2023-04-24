from django.test import TestCase
from django.urls import reverse

class PorteCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_porte_create_page(self):
        response = self.client.get(reverse('porte_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'porte/porte_create.html')