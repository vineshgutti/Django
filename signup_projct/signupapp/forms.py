from django import forms
from .models import Registration
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    firstname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-label','id':'firstname','placeholder':'firstname'}))
    lastname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-label','id':'lastname','placeholder':'lastname'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-label','id':'email','placeholder':'email'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-label','id':'username','placeholder':'username'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-label','id':'password','placeholder':'password'}))
    re_password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-label','id':'re_password','placeholder':'re_password'}))
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
        if len(clean_data['password']) < 8 and len(clean_data['re_password']) < 8:
            raise ValidationError("password length minimum '8' characters")
        if clean_data['password'] != clean_data['re_password']:
            raise ValidationError("passwords should be matched")
        if clean_data['password'].isalnum() and clean_data['re_password'].isalnum() == True:
            raise ValidationError("Any one special charectors '@','#','$' must be there in the given")
            
            