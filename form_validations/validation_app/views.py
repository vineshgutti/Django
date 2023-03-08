from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.
def home(request):
    form = StudentForm()
    text = "<i>Django</i>"
    if request.method == "POST":
        form = StudentForm(request.POST)
        print(form.errors)
        if form.is_valid():
            # email = form.cleaned_data['email']
            form.save()
            return HttpResponse("Form Validated successfully...!")
    return render(request, 'index.html', {'form':form,'text':text})