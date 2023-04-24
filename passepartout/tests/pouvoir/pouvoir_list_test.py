from django.test import TestCase
from django.urls import reverse

class PouvoirListTestCase(TestCase):
    def setUp(self):
        pass

    def test_pouvoir_list_page(self):
        response = self.client.get(reverse('pouvoir_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pouvoir/pouvoir_list.html')