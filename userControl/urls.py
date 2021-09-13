
from django.urls import path
from.import views

urlpatterns = [
   
    path("", views.Authorization.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path('register/', views.Registration.as_view(), name='register'),
    path("main/", views.Index.as_view(), name="index"),
   
]

