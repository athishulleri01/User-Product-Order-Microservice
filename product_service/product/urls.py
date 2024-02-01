from django.urls import path
# from .views import  UserDetailView,UserListView
from .views import ProductViewSet

urlpatterns = [
    path('product',ProductViewSet.as_view({
            'get' : 'list',
            'post' : 'create',
        }) ),
     path('product/<str:pk>',ProductViewSet.as_view({
            'get' : 'retrieve'
        }) ),
    # path('users/', UserListView.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
