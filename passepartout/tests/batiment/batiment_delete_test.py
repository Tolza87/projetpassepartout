from django.test import TestCase
from django.urls import reverse

class BatimentDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_batiment_delete_page(self):
        response = self.client.get(reverse('batiment_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'batiment/batiment_delete.html')