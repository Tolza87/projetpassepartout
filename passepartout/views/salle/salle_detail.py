from django.views.generic import DetailView

from appli.models import Salle


class SalleDetailView(DetailView):
    model = Salle
    template_name = "salle/salle_detail.html"
