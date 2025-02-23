from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="login"),
    path('reg/',views.sign_up, name="register"),
    path('home', views.menu, name="home")
]