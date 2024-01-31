# order_service/order/urls.py
from django.urls import path
from .views import OrderListView, OrderDetailView
from .consumers import start_user_check_consumer

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]

start_user_check_consumer()