from django.test import TestCase
from django.urls import reverse

class PorteListTestCase(TestCase):
    def setUp(self):
        pass

    def test_porte_list_page(self):
        response = self.client.get(reverse('porte_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'porte/porte_list.html')