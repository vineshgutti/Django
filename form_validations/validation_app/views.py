from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
from .models import Student


# Create your views here.
@csrf_exempt
def home(request):
    form = StudentForm()
    text = "<h1>Django</h1>"
    if request.method == "POST":
        form = StudentForm(request.POST)
        print(form.errors)
        if form.is_valid():
            # email = form.cleaned_data['email']
            form.save()
            return redirect("details")
    return render(request, "index.html", {"form": form, "text": text})


def details(request):
    data = Student.objects.all()
    # age=21
    print(data[0].branch)
    return render(request, "details.html", {"data": data})
