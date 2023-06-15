from typing import Any, Dict
from django import forms
from .models import Users
from django.core.exceptions import ValidationError
from django.db.models import Q


# import re


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        model = Users
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "confirm_password",
            "phone",
            "gender",
            "date_of_birth",
        ]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not first_name.isalpha():
            raise forms.ValidationError("first name should contain 'alphabets' only")
        return first_name.strip()

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not last_name.isalpha():
            raise forms.ValidationError("last name should contain 'alphabets' only")
        return last_name.strip()

    def clean_username(self):
        username = self.cleaned_data["username"]
        if Users.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        else:
            if username.isalnum():
                return username.strip()
            else:
                raise forms.ValidationError(
                    "Username should contain only 'alphabets & numerics' only"
                )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        else:
            if "@gmail.com" not in email:
                raise forms.ValidationError(
                    "Please provide valid mail with '@gmail.com'"
                )
            else:
                return email.strip()

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 8:
            raise forms.ValidationError(
                "Password length should be minimum '8' characters"
            )
        if not any(char.isupper() for char in password):
            raise forms.ValidationError(
                "Password must contain at least one uppercase letter"
            )
        if not any(char.islower() for char in password):
            raise forms.ValidationError(
                "Password must contain at least one lowercase letter"
            )
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one digit")
        if not any(not char.isalnum() for char in password):
            raise forms.ValidationError(
                "Password must contain at least one special character"
            )
        return password.strip()

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        # print(self.cleaned_data)
        # print(password)
        # print(confirm_password)
        # print(password != confirm_password)
        # print(password and confirm_password and password != confirm_password)
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password should be the same"
            )
        return confirm_password.strip()

    # def clean_phone(self):
    #     phone = self.cleaned_data.get("phone")
    #     print(type(phone))
    #     string = str(phone)
    #     print(string)
    #     if len(string) > 10 and len(string) < 10:
    #         raise forms.ValidationError("phone number should be in '10' digits")
    #     else:
    #         return phone


# class UserLoginForm(forms.Form):
#     email_or_username = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255)

#     class Meta:
#         fields = ["email_or_username", "password"]


#     def clean_email_or_username(self):
#         email_or_username = self.cleaned_data.get("username_or_email")
#         my_user = Users.objects.filter(
#             Q(username=email_or_username) | Q(email=email_or_username)
#         ).first()
#         if my_user.email or my_user.username is None:
#             raise forms.ValidationError("invalid User")
#         else:
#             if my_user.status != "Active":
#                 raise forms.ValidationError("Please verify your email before login")
class EmailSendResetPasswordForm(forms.Form):
    email = forms.CharField(max_length=255)

    class Meta:
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if "@gmail.com" not in email:
            raise forms.ValidationError("Please provide valid mail with '@gmail.com'")
        else:
            user = Users.objects.filter(email=email).exists()
            print(user)
            if user is False:
                raise forms.ValidationError("please enter registered email address")
        return email


class ChangeEmailForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        print(email)
        if "@gmail.com" not in email:
            raise forms.ValidationError("Please provide valid mail with '@gmail.com'")
        else:
            try:
                user = Users.objects.get(email=email)
                print(user)
            except:
                user = None
            if user is not None:
                raise forms.ValidationError("User is already exist")
        return email


class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        fields = ["password", "confirm_password"]

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 8:
            raise forms.ValidationError(
                "Password length should be minimum '8' characters"
            )
        if not any(char.isupper() for char in password):
            raise forms.ValidationError(
                "Password must contain at least one uppercase letter"
            )
        if not any(char.islower() for char in password):
            raise forms.ValidationError(
                "Password must contain at least one lowercase letter"
            )
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one digit")
        if not any(not char.isalnum() for char in password):
            raise forms.ValidationError(
                "Password must contain at least one special character"
            )
        return password.strip()

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password should be the same"
            )
        return confirm_password.strip()
