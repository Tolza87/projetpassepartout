from django.test import TestCase
from django.urls import reverse

class AppartenirListTestCase(TestCase):
    def setUp(self):
        pass

    def test_appartenir_list_page(self):
        response = self.client.get(reverse('appartenir_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appartenir/appartenir_list.html')