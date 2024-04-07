
from django.urls import path
from . import views

urlpatterns = [
    path('formulario1/', views.form1, name='Form1')
]
