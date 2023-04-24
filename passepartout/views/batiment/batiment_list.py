from django.views.generic import ListView

from appli.models import Batiment

class BatimentListView(ListView):
    model = Batiment
    template_name = "batiment/batiment_list.html"
