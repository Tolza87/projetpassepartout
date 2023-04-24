from django.test import TestCase
from django.urls import reverse

class RolesDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_roles_detail_page(self):
        response = self.client.get(reverse('roles_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roles/roles_detail.html')