from django.views.generic import DetailView

from appli.models import Roles


class RolesDetailView(DetailView):
    model = Roles
    template_name = "roles/roles_detail.html"
