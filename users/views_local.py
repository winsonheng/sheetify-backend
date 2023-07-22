from common.constants import StatusCode
from common.util.json_util import from_model_object
from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render
from django.core.exceptions import BadRequest
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from users.forms import SignupForm
from users.models import User
from django.conf import settings
import json
from users.dummy_form import DummyForm
#from verify_email.email_handler import send_verification_email


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
    
    existing_user = get_user_by_email(email)
    
    # if existing_user and existing_user.verification_status != User.VerificationStatus.PENDING:
    #     # If pending, still send verification email
    #     verification_status = existing_user.verification_status
        
    #     return JsonResponse({
    #         'message': 'Account already exists',
    #         'verification_status': verification_status
    #     }, status=StatusCode.BAD_REQUEST)
    
    
    user = User()
    user.email = email
    user.set_password(password)
    user.verification_status = User.VerificationStatus.PENDING
    if existing_user is None: # Remove this once finish testing email
        user.save()
        token = Token.objects.create(user=user)
    
    send_verification_email(user)
    
    # TODO
    # Not sure why verification email not working
    # signup_form = SignupForm({'email': body.get('email', ''), 'password': body.get('password', '')})
    # inactive_user = send_verification_email(request, signup_form)
    return JsonResponse({
        'message': 'Verification email sent!',
    }, status=StatusCode.OK)


@csrf_exempt
def resend_verification_email(request):
    body = json.loads(request.body)
    email = body.get('email', '')
    password = body.get('password', '')
    
    user = get_user_by_email(email)
    if not user.check_password(password):
        # Check password also matches as additional layer of security
        return JsonResponse({
            'message': 'Something went wrong while processing your request!',
        }, status=StatusCode.BAD_REQUEST)
    
    if user is None:
        # User has not been created
        return JsonResponse({
            'message': 'Account has not been created! Please proceed to sign up instead.',
        }, status=StatusCode.BAD_REQUEST)
    
    # TODO: Add extra check for account verification status
    
    send_verification_email(user)
    
    return JsonResponse({
        'message': 'Verification email sent!',
    }, status=StatusCode.OK)


def get_user_by_email(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    
    return user


def send_verification_email(user: User):
    send_mail(
        'Test Subject',
        'Test message',
        getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply<no_reply@domain.com>'),
        [user.email],
        fail_silently=False,
        html_message='<button>CLICK ME!</button>'
    )


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
    

        