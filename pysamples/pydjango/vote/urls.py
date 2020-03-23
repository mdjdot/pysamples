#!/usr/bin/env python3

from django.urls import path
from django.contrib import admin
from vote import views

urlpatterns = [
    path("", views.show_subjects),
    path('teachers/', views.show_teachers),
        path('praise/', views.prise_or_criticize),
    path('criticize/', views.prise_or_criticize),
    path('admin/', admin.site.urls),
]
