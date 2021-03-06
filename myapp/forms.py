from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, PrependedAppendedText

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _

from django.core.exceptions import ValidationError
#test docstring
class UserLoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.CharField(widget=forms.PasswordInput, required = True)
    remember = forms.BooleanField(label="Remember Me?", required=False)
        
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_show_errors = True
        self.helper.form_show_labels = True
        self.helper.add_input(Submit('submit', 'Login', css_class='btn btn-primary btn-block'))
        # for fieldname in ['username']:
        #     self.fields[fieldname].help_text = None
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username is None:
            raise forms.ValidationError(_("Username cannot be empty"))
        
        if username and (User.objects.filter(username = username).count() == 0):
            raise forms.ValidationError(_("Username Not Registered"))
        
        return username
#test1 docstring
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'e-mail*'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username*'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password*'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password*'}))
    #test2 docstring
    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_show_errors = True
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Register', css_class='btn btn-primary btn-block'))
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(_("Email address is already registered."))
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # not active until he opens activation link test2
            user.save()
        return user
