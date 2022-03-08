from django.urls import path
from . import views

app_name = 'qnaboard'

urlpatterns = [
    path('', views.index, name='index'),
]
