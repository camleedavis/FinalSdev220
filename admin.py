from django.contrib import admin

from .models import Customers,CustomerData
# Register your models here.
admin.site.register(Customers)

admin.site.register(CustomerData)