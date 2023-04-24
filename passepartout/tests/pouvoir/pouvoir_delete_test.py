from django.test import TestCase
from django.urls import reverse

class PouvoirDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_pouvoir_delete_page(self):
        response = self.client.get(reverse('pouvoir_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pouvoir/pouvoir_delete.html')