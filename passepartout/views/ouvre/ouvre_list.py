from django.views.generic import ListView

from appli.models import Ouvre

class OuvreListView(ListView):
    model = Ouvre
    template_name = "ouvre/ouvre_list.html"
