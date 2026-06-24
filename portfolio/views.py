from django.views.generic import ListView
from .models import Project, Link


class HomeView(ListView):
    model = Project
    template_name = 'portfolio/home.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        links = Link.objects.all()
        if not self.request.user.is_authenticated:
            links = links.filter(public=True)
        context['links'] = links
        return context
