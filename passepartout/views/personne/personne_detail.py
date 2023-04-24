from django.views.generic import DetailView

from appli.models import Personne


class PersonneDetailView(DetailView):
    model = Personne
    template_name = "personne/personne_detail.html"
