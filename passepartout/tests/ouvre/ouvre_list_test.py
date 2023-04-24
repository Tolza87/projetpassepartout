from django.test import TestCase
from django.urls import reverse

class OuvreListTestCase(TestCase):
    def setUp(self):
        pass

    def test_ouvre_list_page(self):
        response = self.client.get(reverse('ouvre_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ouvre/ouvre_list.html')