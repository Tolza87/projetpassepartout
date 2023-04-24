from django.test import TestCase
from django.urls import reverse

class PorteDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_porte_delete_page(self):
        response = self.client.get(reverse('porte_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'porte/porte_delete.html')