from django.conf.urls import include
from django.urls import path
from users.router import router
from rest_framework.authtoken import views
from . import views_local

urlpatterns = [
    path('', include(router.urls)),
    path('getToken/', views.obtain_auth_token, name='get_token'),
    path('getCSRF/', views_local.get_csrf, name='get_csrf'),
    path("signupEmail/", views_local.signup_email, name="signup_email"),
    path("resendVerificationEmail/", views_local.resend_verification_email, name="resend_verification_email"),
    path('loginEmail/', views_local.login_email, name='login_email'),
    path('verification/', include('verify_email.urls')),
]