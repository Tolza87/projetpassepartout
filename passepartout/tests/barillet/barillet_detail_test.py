from django.test import TestCase
from django.urls import reverse

class BarilletDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_barillet_detail_page(self):
        response = self.client.get(reverse('barillet_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'barillet/barillet_detail.html')