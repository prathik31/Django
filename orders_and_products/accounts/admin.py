# user----orders            pass--- 123456


from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register(customer),
admin.site.register(products),
admin.site.register(order),
admin.site.register(tag)
