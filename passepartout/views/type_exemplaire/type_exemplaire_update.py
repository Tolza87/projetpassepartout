from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import TypeExemplaire

class TypeExemplaireUpdateView(UpdateView):
    model = TypeExemplaire
    fields = '__all__'
    template_name = "type_exemplaire/type_exemplaire_update.html"
    success_url = reverse_lazy('type_exemplaire_list')
