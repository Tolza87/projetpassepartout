from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import PosseseurDeCLef

class PosseseurDeCLefUpdateView(UpdateView):
    model = PosseseurDeCLef
    fields = '__all__'
    template_name = "posseseur_de_c_lef/posseseur_de_c_lef_update.html"
    success_url = reverse_lazy('posseseur_de_c_lef_list')
