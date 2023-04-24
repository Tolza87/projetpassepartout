from django.test import TestCase
from django.urls import reverse

class BarilletCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_barillet_create_page(self):
        response = self.client.get(reverse('barillet_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'barillet/barillet_create.html')