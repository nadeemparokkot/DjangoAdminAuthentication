"""
URL configuration for sample_8_formmodel_editdelete project.

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
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('create/',views.print_create,name='create_path'),#name= for url eg:menu.html
    path('list/',views.print_list,name='list_path'),
    path('edit/<pk>',views.print_edit,name='edit_path'),
    path('delete/<pk>',views.print_delete,name='delete_path'),
    path('',views.print_list,name='list_path') #ini open cheyyumbo list aayirkum kanikka allenkil namma / use cheyyanam
]
   
