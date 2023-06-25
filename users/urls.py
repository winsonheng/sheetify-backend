from django.conf.urls import include
from django.urls import path
from users.router import router
from rest_framework.authtoken import views
from . import views_local

urlpatterns = [
    path('', include(router.urls)),
    path('getAuthToken/', views.obtain_auth_token, name='get_auth_token'),
    path("signupEmail/", views_local.signup_email, name="signup_email"),
    path('loginEmail/', views_local.login_email, name='login_email'),
]