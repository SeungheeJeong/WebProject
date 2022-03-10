from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('create/', views.CreateChallengeView.as_view,
         name='create'),
]
