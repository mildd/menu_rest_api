from django.urls import path

from menu.views import OrderListView, OrderCreateView, OrderUpdateDestroyDetailView

urlpatterns = [
    path('orders/', OrderListView.as_view()),
    path('orders/<int:pk>', OrderUpdateDestroyDetailView.as_view()),
    path('create_order', OrderCreateView.as_view(), name='create_order'),
]
