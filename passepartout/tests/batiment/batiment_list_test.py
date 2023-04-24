from django.test import TestCase
from django.urls import reverse

class BatimentListTestCase(TestCase):
    def setUp(self):
        pass

    def test_batiment_list_page(self):
        response = self.client.get(reverse('batiment_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'batiment/batiment_list.html')