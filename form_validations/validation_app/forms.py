from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import Student
def validate_mail(value):
    if '@gmail.com' not in value :
        raise ValidationError("Please provide valid mail with '@gmail.com'")

class StudentForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_mail])
    class Meta:
        model = Student
        fields = '__all__'
    def clean_name(self):
        inputname = self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Name should be the minimum length is > 4")
        return inputname 
    def clean(self):
        print("Total validations are done...")
        cleaned_data = super().clean()
        print(self.cleaned_data)
        if len(str(cleaned_data['mobile'])) > 10 or len(str(cleaned_data['mobile']))<10 :
            raise forms.ValidationError("Number should be 10 digits ")
        if cleaned_data['rool_number'] < 100 or cleaned_data['rool_number'] >= 200 :
            raise forms.ValidationError("please provide the rool_number in range of '101 to 199' only")
        if cleaned_data['age'] < 18 or cleaned_data['age'] > 25:
            raise forms.ValidationError("please provide the valid student age '18 to 25'")
        
        