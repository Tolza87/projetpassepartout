from django.views.generic import ListView

from appli.models import Porte

class PorteListView(ListView):
    model = Porte
    template_name = "porte/porte_list.html"
