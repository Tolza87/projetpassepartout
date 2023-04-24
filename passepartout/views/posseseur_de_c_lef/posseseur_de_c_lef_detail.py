from django.views.generic import DetailView

from appli.models import PosseseurDeCLef


class PosseseurDeCLefDetailView(DetailView):
    model = PosseseurDeCLef
    template_name = "posseseur_de_c_lef/posseseur_de_c_lef_detail.html"
