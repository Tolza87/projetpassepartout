from django.test import TestCase
from django.urls import reverse

class OuvreDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_ouvre_delete_page(self):
        response = self.client.get(reverse('ouvre_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ouvre/ouvre_delete.html')