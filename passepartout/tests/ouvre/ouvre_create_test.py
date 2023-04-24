from django.test import TestCase
from django.urls import reverse

class OuvreCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_ouvre_create_page(self):
        response = self.client.get(reverse('ouvre_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ouvre/ouvre_create.html')