
from django.contrib import admin
from django.urls import path,include
from emails.consumers import start_user_check_consumer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('emails.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

start_user_check_consumer()