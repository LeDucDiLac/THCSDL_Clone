from .views import LogoutView,RegistratrionView, UsernameValidationView, EmailValidationView, LoginView,VerificationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register',RegistratrionView.as_view(),name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name='logout'),
    path('activate',VerificationView.as_view(),name='activate'),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()),name='validate-email'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),name="validate-username")
]
