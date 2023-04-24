from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import TypeExemplaire

class TypeExemplaireCreateView(CreateView):
    model = TypeExemplaire
    fields = '__all__'
    template_name = "type_exemplaire/type_exemplaire_create.html"
    success_url = reverse_lazy('type_exemplaire_list')
