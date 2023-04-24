from django.views.generic import DetailView

from appli.models import Porte


class PorteDetailView(DetailView):
    model = Porte
    template_name = "porte/porte_detail.html"
