from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(profile)
admin.site.register(categories)
admin.site.register(quiz)
admin.site.register(questions)
admin.site.register(choices)