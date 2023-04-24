from django.views.generic import ListView

from appli.models import PosseseurDeCLef

class PosseseurDeCLefListView(ListView):
    model = PosseseurDeCLef
    template_name = "posseseur_de_c_lef/posseseur_de_c_lef_list.html"
