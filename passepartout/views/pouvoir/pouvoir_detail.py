from django.views.generic import DetailView

from appli.models import Pouvoir


class PouvoirDetailView(DetailView):
    model = Pouvoir
    template_name = "pouvoir/pouvoir_detail.html"
