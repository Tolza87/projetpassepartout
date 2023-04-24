from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import PosseseurDeCLef

class PosseseurDeCLefCreateView(CreateView):
    model = PosseseurDeCLef
    fields = '__all__'
    template_name = "posseseur_de_c_lef/posseseur_de_c_lef_create.html"
    success_url = reverse_lazy('posseseur_de_c_lef_list')
