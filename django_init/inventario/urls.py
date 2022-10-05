from django.urls import path
from .views import InventoryView

urlpatterns = [
    path('inventary/', InventoryView.as_view(), name='inventory_list'),
    path('inventary/<int:id>', InventoryView.as_view(), name='inventory_process'),
]
