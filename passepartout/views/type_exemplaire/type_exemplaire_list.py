from django.views.generic import ListView

from appli.models import TypeExemplaire

class TypeExemplaireListView(ListView):
    model = TypeExemplaire
    template_name = "type_exemplaire/type_exemplaire_list.html"
