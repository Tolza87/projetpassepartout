from django.test import TestCase
from django.urls import reverse

class BatimentCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_batiment_create_page(self):
        response = self.client.get(reverse('batiment_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'batiment/batiment_create.html')