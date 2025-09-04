from django.urls import path
from . import views
from django.urls import path, include
from django.contrib import admin
app_name = 'mainapp'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('contactanos_2/', views.contactanos_2, name='contactanos_2'),
    path('enlaces/', views.enlaces, name='enlaces'),
    path('equipo/', views.equipo, name='equipo'),
    path('admin/', admin.site.urls),
] 