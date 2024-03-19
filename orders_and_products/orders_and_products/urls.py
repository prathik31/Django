"""
URL configuration for orders_and_products project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# username--- johnwick          password---123ewqasd

from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('products/',product),
    path('customer/<int:id>',customers),
    path('create_order/',create_order),
    path('update_order/<int:id>',update_order),
    path('delete_order/<int:id>',delete_order),
    path('create_customer/',create_customer),
    path('update_customer/<int:id>',update_customer),
    path('delete_customer/<int:id>',delete_customer),
    path('Add_product/',Add_product),
    path('login/',loginpage),
    path('logout/',logoutpage),
    path('register/',register)
]
