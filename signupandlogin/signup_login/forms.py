# from django import forms
# from .models import Users
# from django.core.validators import *


# class UserRegistrationForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         max_length=255,
#         validators=[
#             MinLengthValidator(8),
#         ],
#     )

#     class Meta:
#         model = Users
#         fields = [
#             "first_name",
#             "last_name",
#             "username",
#             "email",
#             "password",
#             "confirm_password",
#             "phone",
#             "gender",
#             "date_of_birth",
#         ]
