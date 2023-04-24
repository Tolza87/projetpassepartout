from django.views.generic import ListView

from appli.models import Barillet

class BarilletListView(ListView):
    model = Barillet
    template_name = "barillet/barillet_list.html"
