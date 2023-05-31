from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.core import validators


def validate_mail(value):
    if "@gmail.com" not in value:
        raise forms.ValidationError("Please provide valid mail with '@gmail.com'")


class webform(forms.ModelForm):
    email = forms.EmailField(validators=[validate_mail])

    class Meta:
        model = User
        fields = ["email", "name", "password", "phone_number"]

    def save(self, commit=True):
        user = super(webform, self).save(commit=False)
        password = self.cleaned_data["password"]
        print(len(password))
        if len(password) != 0:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(webform, self).clean()
        email = cleaned_data.get("email")
        name = cleaned_data.get("name")
        phone_number = cleaned_data.get("phone_number")

        if len(name) < 5:
            raise forms.ValidationError("minimum 5 characters required")

        if len(str(phone_number)) > 10 or len(str(phone_number)) < 10:
            # if len(str(phone_number)) != 10:
            raise forms.ValidationError("Number should be 10 digits ")

        return self.cleaned_data
