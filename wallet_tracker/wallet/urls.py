# from django.urls import path
# from .views import transaction_list,add_transaction,home,manage_budget,add_budget, budget_list

# urlpatterns = [
#     path('', home, name='home'),
#     path('transactions/', transaction_list, name='transaction_list'),
#     path('add_transaction/',add_transaction, name='add_transaction'),
#     path('manage_budget/', manage_budget, name='manage_budget'),
#     path('add_budget/', add_budget, name='add_budget'),
#     path('budget_list/', budget_list, name='budget_list'),


    
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('set_budget/', views.set_budget, name='set_budget'),
    path('generate_report/', views.generate_report, name='generate_report'),
]
