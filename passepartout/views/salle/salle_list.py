from django.views.generic import ListView

from appli.models import Salle

class SalleListView(ListView):
    model = Salle
    template_name = "salle/salle_list.html"
