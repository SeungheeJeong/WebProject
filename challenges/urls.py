from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('create/', views.CreateChallengeView.as_view(),
         name='create'),
    path('list/', views.ChallengeList,
         name='list'),
    path('<int:challenge_id>/', views.ChallengeList,
         name='detail'),
    path('<int:challenge_id>/', views.ChallengeJoin,
         name='join'),
]
