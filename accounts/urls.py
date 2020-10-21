from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, activate_email, profile


urlpatterns = [
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/activate/<user_id>/<token>/', activate_email, name='activate_email'),
    
    path('accounts/profile/', profile, name='profile'),
]
