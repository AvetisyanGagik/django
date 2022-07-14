from django.contrib import admin
from . import views
from . models import Product,Category, Category_details

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Category_details)

