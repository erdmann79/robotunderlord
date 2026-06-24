from django.views.generic import ListView
from .models import Project


class HomeView(ListView):
    model = Project
    template_name = 'portfolio/home.html'
    context_object_name = 'projects'
