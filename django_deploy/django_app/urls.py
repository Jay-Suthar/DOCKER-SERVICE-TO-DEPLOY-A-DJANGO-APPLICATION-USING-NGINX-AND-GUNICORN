from django.urls import path
from .views import ItemListView, AddItemView

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('add/', AddItemView.as_view(), name='item_add'),
]
