from django.views.generic import ListView

from appli.models import Variure

class VariureListView(ListView):
    model = Variure
    template_name = "variure/variure_list.html"
