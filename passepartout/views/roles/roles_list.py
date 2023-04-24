from django.views.generic import ListView

from appli.models import Roles

class RolesListView(ListView):
    model = Roles
    template_name = "roles/roles_list.html"
