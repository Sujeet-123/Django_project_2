from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'




# from django.contrib import admin
# from .models import Customer

# # Register your models here.

# admin.site.register(Customer)