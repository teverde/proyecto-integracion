"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from personal.views import (
    home_screen_view,
    users_index_view,
    cities_index_view,
    user_view,
    city_view,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('users/', users_index_view, name="users"),
    path('cities/', cities_index_view, name="cities"),
    path('users/<int:id>/', user_view, name="user"),
    path('cities?q=<str:id>/', city_view, name="city"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
