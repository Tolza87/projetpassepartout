from django.views.generic import DetailView

from appli.models import Appartenir


class AppartenirDetailView(DetailView):
    model = Appartenir
    template_name = "appartenir/appartenir_detail.html"
