from django.urls import path
from . import views

urlpatterns = [
    path('animal/',views.get_accueil),
    path('',views.get_accueil),
    path('animal/<slug:slug>', views.get_typeAnimal),
    path('animal/<slug:slug1>/<slug:slug2>',views.get_adoptationForm),
    path('contact/',views.get_contact)
]