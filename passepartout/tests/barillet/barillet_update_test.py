from django.test import TestCase
from django.urls import reverse

class BarilletUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_barillet_update_page(self):
        response = self.client.get(reverse('barillet_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'barillet/barillet_update.html')