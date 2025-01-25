from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('reports/', views.reports, name='reports'),
    
]
