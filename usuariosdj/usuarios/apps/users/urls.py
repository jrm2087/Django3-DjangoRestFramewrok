from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('login/', views.Login.as_view(), name='user-login'),
    path('logout/', views.logoutView.as_view(), name='user-logout'),
    path('update-password/', views.UpdatePassword.as_view(), name='update-password'),
    path('user-verification/<pk>/', views.CodeVerificationView.as_view(),
         name='user-verification'),
]
