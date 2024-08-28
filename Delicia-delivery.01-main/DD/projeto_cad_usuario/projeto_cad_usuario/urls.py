
from django.urls import path
from app_cad_usuario import views

urlpatterns = [
   path('',views.home,name='home'),
   path('usuarios/',views.usuarios,name='lista_usuarios'),
]
