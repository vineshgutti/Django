from django.shortcuts import render
from .models import Employee
from django.template import loader

# from .forms import EmployeeForm
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return render(request, "ajaxapp/home.html")


def create(request):
    # form = EmployeeForm()
    if request.method == "POST":
        # print(request.POST)
        e_name = request.POST.get("Name")
        # print(e_name)
        e_date_of_birth = request.POST.get("Date_of_birth")
        e_mobile = request.POST.get("Mobile")
        e_area = request.POST.get("Area")
        e_days = request.POST.get("Days")
        e_salary = request.POST.get("Salary")
        l = []
        if len(e_name) <= 3:
            msg1 = "Please provide the valid name minimum length '4' characters"
            l.append(msg1)
        if len(e_mobile) < 10:
            msg2 = "The mobile number should be '10' digits"
            l.append(msg2)
        print(l)
        print(l[0])
        # form = EmployeeForm(request.POST)
        form = Employee(
            name=e_name,
            date_of_birth=e_date_of_birth,
            mobile=e_mobile,
            area=e_area,
            days=e_days,
            salary=e_salary,
        )
        form.save()

        # data = Employee.objects.values()
        # list_data = list(data)
        # print(list_data)
        # return JsonResponse({"list_data": list_data})

        message = "data submited successfully"
        return JsonResponse({"message": message, "list": l})


def details(request):
    # if request.method == "GET":
    print(request.method)
    data = Employee.objects.all()
    html_string = loader.render_to_string("ajaxapp/table.html", {"data": data})
    # print(data)
    # list_data = list(data)
    print(html_string)
    return JsonResponse({"html_string": html_string})
    # return render(request, "ajaxapp/home.html", {html_string})
