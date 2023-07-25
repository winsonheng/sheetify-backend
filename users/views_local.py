from common.constants import StatusCode
from common.util.json_util import from_model_object
from django.contrib.auth import get_user_model, authenticate
from django.contrib.sites.shortcuts import get_current_site  
from django.shortcuts import render
from django.core.exceptions import BadRequest
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from users.forms import SignupForm
from users.models import User
from django.conf import settings
import json
from users.dummy_form import DummyForm
from users.token_generator import TokenGenerator
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
    
    print('Signing up: ' + email)
    
    existing_user = get_user_by_email(email)
    
    if existing_user and existing_user.verification_status != User.VerificationStatus.PENDING:
        # If pending, still send verification email
        verification_status = existing_user.verification_status
        
        return JsonResponse({
            'message': 'Account already exists',
            'verification_status': verification_status
        }, status=StatusCode.BAD_REQUEST)
    
    
    user = User()
    user.email = email
    user.set_password(password)
    user.verification_status = User.VerificationStatus.PENDING
    if existing_user is None:
        user.save()
        token = Token.objects.create(user=user)
        send_verification_email(user)
    else:
        return resend_verification_email(request)
    
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
    activation_token = TokenGenerator().make_token(user)
    
    domain = getattr(settings, 'CLIENT_URL', 'localhost:3000') + getattr(settings, 'VERIFY_EMAIL_URL', '')
    
    message = render_to_string('verification_email.html', {  
        'user': user,  
        'domain': f'{domain}/{urlsafe_base64_encode(force_bytes(user.pk))}/{activation_token}' 
    })
    
    send_mail(
        'Test Subject',
        message,
        getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply<no_reply@domain.com>'),
        [user.email],
        fail_silently=False
    )


@csrf_exempt
def verify_email(request):
    print('Verifying your email:')
    body = json.loads(request.body)
    uidb64 = body.get('uidb64')
    token = body.get('token')
    
    uid = force_str(urlsafe_base64_decode(uidb64))
    
    user = User.objects.get(pk=uid)
    
    verify_ok = TokenGenerator().check_token(user, token)
    
    if not verify_ok:
        return JsonResponse({
            'message': 'Invalid or expired verification link. Please sign up again.'
        }, status=StatusCode.BAD_REQUEST)
        
    user.verification_status = User.VerificationStatus.VERIFIED
    user.save()
    
    return JsonResponse({
        'message': 'Your account has been verified.',
        'email': user.email
    }, status=StatusCode.OK)


@csrf_exempt
def reset_password(request):
    pass

# Not using api_view decorator as it uses auth classes in settings.py
@csrf_exempt
def login_email(request):
    body = json.loads(request.body)
    email = body.get('email')
    username = body.get('username')
    password = body.get('password')

    # Uses auth.py to authenticate via email
    user = authenticate(username=email, password=password)
    if user is None:
        return JsonResponse({
            'message': 'Please check your login details and try again'
        }, status=StatusCode.UNAUTHORIZED)

    # TODO: allow login via username
    
    if user.verification_status != User.VerificationStatus.VERIFIED:
        return JsonResponse({
            'message': 'You have not verified your email!'
        }, status=StatusCode.UNAUTHORIZED)
    
    return JsonResponse({
        'message': 'Login successful!',
        'user': {
            'username': user.get_username(),
            'last_login': user.last_login
        }
    }, status=StatusCode.OK)
    

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def set_username(request):
    user = Token.objects.get(key=request.auth.key).user
    body = json.loads(request.body)
    username = body.get('username', '')
    
    user.username = username
    user.save()
    
    return JsonResponse({
        'message': 'Username successfully set!',
    }, status=StatusCode.OK)
