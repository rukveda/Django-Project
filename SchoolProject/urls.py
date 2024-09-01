from django.contrib import admin
from django.urls import path, re_path
from StudentApp import views

urlpatterns = [
    re_path(r'^student$', views.studentApi),  # Handles /student
    re_path(r'^student/([0-9]+)$', views.studentApi),  # Handles /student/<number>
    path('admin/', admin.site.urls),  # Handles /admin
]
