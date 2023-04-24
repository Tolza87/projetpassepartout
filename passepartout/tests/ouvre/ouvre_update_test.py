from django.test import TestCase
from django.urls import reverse

class OuvreUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_ouvre_update_page(self):
        response = self.client.get(reverse('ouvre_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ouvre/ouvre_update.html')