from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import TypeExemplaire

class TypeExemplaireDeleteView(DeleteView):
    model = TypeExemplaire
    template_name = "type_exemplaire/type_exemplaire_delete.html"
    success_url = reverse_lazy('type_exemplaire_list')