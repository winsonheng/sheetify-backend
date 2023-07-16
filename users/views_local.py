from common.constants import StatusCode
from common.util.json_util import from_model_object
from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render
from django.core.exceptions import BadRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from users.forms import SignupForm
from users.models import User
import json
from verify_email.email_handler import send_verification_email


# Create your views here.

def get_csrf(request):
    csrftoken = csrf.get_token(request)
    return JsonResponse({
        'csrftoken': csrftoken
    }, status=StatusCode.OK)
    

@csrf_exempt
def signup_email(request):
    body = json.loads(request.body)
    email = body.get('email', '')
    password = body.get('password', '')
    if check_if_account_exists(email):
        return JsonResponse({
            'message': 'Account already exists',
            'accountExists': True                 
        }, status=StatusCode.BAD_REQUEST)
      
    user = User()
    user.email = email
    user.set_password(password)
    user.verification_status = User.VerificationStatus.PENDING
    user.save()
    token = Token.objects.create(user=user)
    print(token.key)
    # TODO
    # Not sure why verification email not working
    # signup_form = SignupForm({'email': body.get('email', ''), 'password': body.get('password', '')})
    # inactive_user = send_verification_email(request, signup_form)
    return JsonResponse({
        'message': 'Account created successfully',
    }, status=StatusCode.OK)


def check_if_account_exists(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return False
    
    return True

# Not using api_view decorator as it uses auth classes in settings.py
def login_email(request):
    body = json.loads(request.body)
    email = body.get('email')
    username = body.get('username')
    password = body.get('password')
    print(email, password)
    # Uses auth.py to authenticate via email
    user = authenticate(username=email, password=password)
    if user is None:
        return JsonResponse({
            'message': 'Please check your login details and try again'
        }, status=StatusCode.UNAUTHORIZED)
    
    # TODO: allow login via username
    
    return JsonResponse({
        'message': 'Login successful!',
        'user': {
            'username': user.get_username(),
            'last_login': user.last_login
        }
    }, status=StatusCode.OK)
    
        