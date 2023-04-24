from django.views.generic import DetailView

from appli.models import TypeExemplaire


class TypeExemplaireDetailView(DetailView):
    model = TypeExemplaire
    template_name = "type_exemplaire/type_exemplaire_detail.html"
