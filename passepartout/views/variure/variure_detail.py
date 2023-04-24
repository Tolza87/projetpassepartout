from django.views.generic import DetailView

from appli.models import Variure


class VariureDetailView(DetailView):
    model = Variure
    template_name = "variure/variure_detail.html"
