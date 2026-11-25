from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('_admin/', admin.site.urls),
]
