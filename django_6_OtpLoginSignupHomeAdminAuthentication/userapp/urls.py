"""
URL configuration for sample_13_signuploginauth project.

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
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/',views.print_home,name='home_path'),
    path('',views.print_login,name='login_path'),
    path('signup/',views.print_signup,name='signup_path'),
    path('logout/',views.print_logout,name='logout_path'),
    path('otpverify/',views.print_otp,name='otp_path'),
    path('timeout/',views.print_timeout,name='timeout_path'),
    path('resendotp/',views.print_resend_otp,name='resend_otp_path')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)