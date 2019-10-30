from django.urls import path
from maung import views

urlpatterns = [
    path('members/', views.find_all_members),
    path('search/', views.search_members),
]