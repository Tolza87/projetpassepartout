from django.views.generic import ListView

from appli.models import Exemplaire

class ExemplaireListView(ListView):
    model = Exemplaire
    template_name = "exemplaire/exemplaire_list.html"
