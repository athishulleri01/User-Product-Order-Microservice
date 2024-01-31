
from django.contrib import admin
from django.urls import path,include
from order.consumers import start_user_check_consumer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('order.urls')), 
]

# start_user_check_consumer()