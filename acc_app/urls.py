from django.urls import path
from acc_app.views import register, UserProfile
from django.contrib.auth import views as auth_views

app_name = 'acc_app'

urlpatterns = [
    path('profile/<slug>', UserProfile.as_view(), name='profile'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
]
