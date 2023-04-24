from django.test import TestCase
from django.urls import reverse

class RolesDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_roles_delete_page(self):
        response = self.client.get(reverse('roles_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roles/roles_delete.html')