from django.views.generic import DetailView

from appli.models import Batiment


class BatimentDetailView(DetailView):
    model = Batiment
    template_name = "batiment/batiment_detail.html"
