from django.test import TestCase
from django.urls import reverse

class SalleListTestCase(TestCase):
    def setUp(self):
        pass

    def test_salle_list_page(self):
        response = self.client.get(reverse('salle_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salle/salle_list.html')