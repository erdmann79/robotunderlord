from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
