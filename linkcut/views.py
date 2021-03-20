from django.shortcuts import render
from django.views.generic import (
    ListView,
    # DetailView,
    # CreateView,
    # UpdateView,
    # DeleteView
)
from .models import CutLink
# Create your views here.

# def home(request):
#     return render(request, 'linkcut/home.html')

def about(request):
    return render(request, 'linkcut/about.html')

class CutLinkView(ListView):
    model = CutLink
    template_name = 'linkcut/home.html'
    context_object_name = 'link'
    # ordering = ['id']

    def get_context_data(self, **kwards):
        ctx = super(CutLinkView, self).get_context_data(**kwards)
        ctx['title_name'] = 'Главная страница'
        return ctx