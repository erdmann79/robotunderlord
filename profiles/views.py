from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def my_profile(request):
    return render(request, 'profiles/profile.html', {'profile': request.user.profile})


from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
