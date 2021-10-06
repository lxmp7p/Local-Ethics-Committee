
from django.urls import path
from.import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.Authorization.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', views.Registration.as_view(), name='register'),
    path("main/", login_required(TemplateView.as_view(template_name="index.html")), name="index"),
]

