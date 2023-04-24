from django.test import TestCase
from django.urls import reverse

class VariureListTestCase(TestCase):
    def setUp(self):
        pass

    def test_variure_list_page(self):
        response = self.client.get(reverse('variure_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'variure/variure_list.html')