from django.urls import path

from . import views

urlpatterns = [

    path("signupEmail/", views.signup_email, name="signup_email"),

]