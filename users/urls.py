from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('register', userViews.register, name='register'),
    path('login', authViews.LoginView.as_view(template_name='users/user.html'), name='login'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    
    path('reset-pass', authViews.PasswordResetView.as_view(
        template_name='users/reset_pass.html'), name='reset-pass'),
    
    path('password_reset_success', authViews.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_success.html'), name='password_reset_success'),
    
    path('password_reset_confirm/<uidb64>/token/', authViews.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password_reset_done/', authViews.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    
    path('profile', userViews.profile, name='profile'),
]