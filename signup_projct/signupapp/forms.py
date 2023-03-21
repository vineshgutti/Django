from django import forms
from .models import Registration
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    firstname = forms.CharField(required=True,help_text='Firstname',widget=forms.TextInput(attrs={'class':'form-control','id':'firstname','placeholder':'firstname'}))
    lastname = forms.CharField(required=True,help_text='Lastname',widget=forms.TextInput(attrs={'class':'form-control','id':'lastname','placeholder':'lastname'}))
    email = forms.CharField(required=True,help_text='Email',widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'email'}))
    password = forms.CharField(required=True,help_text='Password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'password'}))
    re_password = forms.CharField(required=True,help_text='Re-Password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'re_password','placeholder':'re_password'}))
    class Meta:
        model = Registration
        fields = '__all__'
        
        def clean(self):
            clean_data = super().clean()
            if len(clean_data['firstname']) < 4:
                raise ValidationError("The firstname length should be minimum '4' characters")
            if len(clean_data['lastname']) < 4:
                raise ValidationError("The lastname length should be minimum '4' characters")
            if '@gmail.com' not in clean_data['email']:
                raise ValidationError("Please provide valid mail with '@gmail.com'")
            if len(clean_data['username']) < 8:
                raise ValidationError("The user name length should be minimum '8' characters")
            if clean_data['password'] and clean_data['re_password'] < 8:
                raise ValidationError("password length minimum '8' characters")
            if clean_data['password'] != clean_data['re_password']:
                raise ValidationError("passwords should be the same")
                
            