from django.views.generic import DetailView

from appli.models import Ouvre


class OuvreDetailView(DetailView):
    model = Ouvre
    template_name = "ouvre/ouvre_detail.html"
