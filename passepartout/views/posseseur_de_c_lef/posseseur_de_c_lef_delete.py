from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import PosseseurDeCLef

class PosseseurDeCLefDeleteView(DeleteView):
    model = PosseseurDeCLef
    template_name = "posseseur_de_c_lef/posseseur_de_c_lef_delete.html"
    success_url = reverse_lazy('posseseur_de_c_lef_list')