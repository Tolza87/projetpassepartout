from django.views.generic import DetailView

from appli.models import Exemplaire


class ExemplaireDetailView(DetailView):
    model = Exemplaire
    template_name = "exemplaire/exemplaire_detail.html"
