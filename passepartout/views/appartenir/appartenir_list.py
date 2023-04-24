from django.views.generic import ListView

from appli.models import Appartenir

class AppartenirListView(ListView):
    model = Appartenir
    template_name = "appartenir/appartenir_list.html"
