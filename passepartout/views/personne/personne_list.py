from django.views.generic import ListView

from appli.models import Personne

class PersonneListView(ListView):
    model = Personne
    template_name = "personne/personne_list.html"
