from django.contrib import admin

# Register your models here.
from .models import Order,User

admin.site.register(Order)
admin.site.register(User)