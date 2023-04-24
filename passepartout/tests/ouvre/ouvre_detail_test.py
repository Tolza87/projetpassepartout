from django.test import TestCase
from django.urls import reverse

class OuvreDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_ouvre_detail_page(self):
        response = self.client.get(reverse('ouvre_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ouvre/ouvre_detail.html')