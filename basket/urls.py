from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('adjust/<item_id>/', views.update_basket, name='update_basket'),
]
