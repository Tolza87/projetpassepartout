from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Exemplaire

class ExemplaireUpdateView(UpdateView):
    model = Exemplaire
    fields = '__all__'
    template_name = "exemplaire/exemplaire_update.html"
    success_url = reverse_lazy('exemplaire_list')
