from django.contrib import admin
from django.urls import path
from frontend.views import inicio, ayuda       #Del proyecto usar las vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('ayuda/', ayuda)
]
