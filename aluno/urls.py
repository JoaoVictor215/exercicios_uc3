from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path('lista', views.aluno, name="aluno"),
]