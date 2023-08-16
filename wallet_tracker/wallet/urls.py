

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('set_budget/', views.set_budget, name='set_budget'),
    path('generate_report/', views.generate_report, name='generate_report'),
]
