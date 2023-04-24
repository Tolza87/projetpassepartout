from django.test import TestCase
from django.urls import reverse

class PorteDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_porte_detail_page(self):
        response = self.client.get(reverse('porte_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'porte/porte_detail.html')