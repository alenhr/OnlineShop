import urllib2
import json
from django.conf import settings
from django.contrib import auth
from django.template.context_processors import csrf
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from myapp.models import *
from django.db.models import Count
import logging
from datetime import datetime, timedelta
import sys
from django.contrib import messages
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.template import *
from django import forms
from myapp.forms import RegistrationForm, UserLoginForm
from django.core.mail import send_mail
import hashlib, random
from django.utils import timezone
from django.template import RequestContext
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request, 'index.html')

def checkout(request):
	return render(request, 'checkout.html')

def contact(request):
	return render(request, 'contact.html')

def details(request):
	return render(request, 'details.html')

def women(request):
	return render(request, 'women.html')

def login_user(request):
    
    form = UserLoginForm(request.POST or None)
    isError = False
    errormsg = ""
    context = {
        'form' : form,
        'isError' : isError,
        'errormsg' : errormsg
    }
    if request.method == 'POST':
        if form.is_valid():
            print form.cleaned_data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            print "user:"
            print user
            if user is not None and user.is_active:
                auth.login(request, user)
                return render(request,'index.html')
            else:
                context['isError'] = True
                context['errormsg'] = "Username and Passowrd Mismatch"
            
            
    return render(request,'login.html', context)

def register(request):
	args = {}
	args.update(csrf(request))

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		args['form'] = form
		if form.is_valid():
			form.save() # save user to database if form is valid

			# Email Verification Starts Here
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
			activation_key = hashlib.sha1(salt+email).hexdigest()            
			key_expires = datetime.today() + timedelta(2)

			print key_expires

			#Get user by username
			user=User.objects.get(username=username)
			user.is_active = True
			user.save()

			# Create and save user profile                                                                                                                                  
			new_profile = UserProfile(user=user, activation_key=activation_key, key_expires=key_expires)
			new_profile.save()

			# Send email with activation key
			#send_mial(subject,message,from_email,to_list,fail_silently=True)
			email_subject = 'Company Name - Account confirmation'
			email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
			48hours http://127.0.0.1:8000/user_confirm/%s" % (username, activation_key)

			from_email = settings.EMAIL_HOST_USER

			# template = get_template('verification_email.html')
			# context = Context({'username': username, 'activation_key': activation_key})
			html_message = '''
			<div style="border:1px solid black; margin:5px">
			<strong>Dear %s,</strong></br>activation_key
			<p> Greetings from Company Name. Thank you for registering with us<p>
			<p> Please click on below button to complete registration</p>
			<div style="text-align:center">
			<input type="button" href="http://127.0.0.1:8000/user_confirm/%s" value="Click here to complete registration">
			</div>
			<p> If the button is not visible, please click on below link or copy-paste the url in browser:</p>
			http://127.0.0.1:8000/user_confirm/%s
			<p> If you face any difficulties, write to us at <a style="color:blue; font-weight:bold">support@companyname.com</a > or call us on <a style="color:blue; font-weight:bold">(+91) 8179608300</a></p></br>
			<strong>Have a great day!!!</strong>
			</br>
			</br>
			<p>Regards,</p>
			<p>SuportTeam, NearByMedics</p>
			</div>
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
			''' % (username, activation_key, activation_key)

			# html_message = template.render(context)

			# send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [user.email], fail_silently=True, html_message = html_message)


			args['form'] = RegistrationForm()
			args['register_success'] = True

			return render(request,'register.html', args )
	else:
		form = RegistrationForm()

	args['form'] = form
	args['register_success'] = False

	return render(request,'register.html', args)