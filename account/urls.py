from django.urls import path
from account import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileEditView.as_view(), name='profile'),
    path('password_change/', views.ProfilePasswordChangeView.as_view(), name='password_change')
]