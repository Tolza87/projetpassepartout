from django.test import TestCase
from django.urls import reverse

class BarilletDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_barillet_delete_page(self):
        response = self.client.get(reverse('barillet_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'barillet/barillet_delete.html')