from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('<str:username>/', views.detail, name='detail'),
    # path('update/<str:username>/', views.update, name='update'),
    # path('delete/<str:username>/', views.update, name='delete'),
]
