from django.test import TestCase
from django.urls import reverse

class BarilletListTestCase(TestCase):
    def setUp(self):
        pass

    def test_barillet_list_page(self):
        response = self.client.get(reverse('barillet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'barillet/barillet_list.html')