from django.test import TestCase
from django.urls import reverse

class BatimentUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_batiment_update_page(self):
        response = self.client.get(reverse('batiment_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'batiment/batiment_update.html')