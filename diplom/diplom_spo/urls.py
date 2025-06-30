from django.urls import path
from . import views

app_name = 'diplom_spo'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.diplom_edit, name='diplom_edit'),
    path('add/', views.diplom_create, name='diplom_create'),
]
