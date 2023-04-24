from django.views.generic import DetailView

from appli.models import Barillet


class BarilletDetailView(DetailView):
    model = Barillet
    template_name = "barillet/barillet_detail.html"
