from django.test import TestCase
from django.urls import reverse

class AppartenirDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_appartenir_delete_page(self):
        response = self.client.get(reverse('appartenir_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appartenir/appartenir_delete.html')