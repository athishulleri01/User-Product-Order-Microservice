# user_service/user/urls.py
from django.urls import path
# from .views import  UserDetailView,UserListView
from .views import UserViewSet

urlpatterns = [
    path('users',UserViewSet.as_view({
            'get' : 'list',
            'post' : 'create',
        }) ),
     path('users/<str:pk>',UserViewSet.as_view({
            'get' : 'retrieve'
        }) ),
    # path('users/', UserListView.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
