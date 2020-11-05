from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, activate_email, profile


urlpatterns = [
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(),
        name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
        name='logout'),
    path('accounts/activate/<user_id>/<token>/',
        activate_email, name='activate_email'),
    path('accounts/password-reset',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    path('accounts/password-reset/done',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('accounts/password-reset/confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('accounts/password-reset/complete',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    path('accounts/profile/', profile, name='profile'),
]
