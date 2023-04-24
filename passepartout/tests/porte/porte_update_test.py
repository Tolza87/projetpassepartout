from django.test import TestCase
from django.urls import reverse

class PorteUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_porte_update_page(self):
        response = self.client.get(reverse('porte_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'porte/porte_update.html')