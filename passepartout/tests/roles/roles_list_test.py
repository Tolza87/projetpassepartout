from django.test import TestCase
from django.urls import reverse

class RolesListTestCase(TestCase):
    def setUp(self):
        pass

    def test_roles_list_page(self):
        response = self.client.get(reverse('roles_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roles/roles_list.html')