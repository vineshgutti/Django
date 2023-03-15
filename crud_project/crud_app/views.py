from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.core.serializers import serialize

import json 



# Create your views here.
@csrf_exempt
def crate(request):
    # form = ProductForm()
    print(request.POST)
    print(request.body) 
    print(type(request.body))
    if request.method == 'POST':
        form = ProductForm(json.loads(request.body))
        # print(form)
        print(request.body)
        print(type(request.body))
        print(json.loads(request.body))
        print(type(json.loads(request.body))) 
        print(request.POST)
        if form.is_valid():
            form.save()
            msg={'message':'data submitted successfully...'}
            return HttpResponse(json.dumps(msg),content_type="application/json")
        else:
            # form = ProductForm()
            return HttpResponse("form not submited...")
    # else:
        # return render(request, 'crud_app/form.html', {'form':form})
    
def details(request):
    data = Product.objects.all()
    print(data)
    print()
    print(type(data))
    print()
    print(data.values())
    print()
    print(type(data.values()))
    print()
    print(list(data.values()))
    print()
    print(type(list(data.values())))
    # print(data.json())
    # print(type(data.json()))
    # print(json.dumps(data))
    return JsonResponse({'data':list(data.values())})

@csrf_exempt
def patch(request,id):
    obj=Product.objects.get(id=id)
    old_data = obj.__dict__
    print(old_data)
    old_data.pop('_state')
    # old_data.pop('created_at')
    # old_data.pop('updated_at')
    # old_data.pop('id')

    # print(old_data)
    # print(type(old_data))
    # print(request.body)
    # print(type(request.body))
    # print(json.loads(request.body))
    # print(type(json.loads(request.body)))
    old_data.update(json.loads(request.body))
    print(old_data)
    # print(type(old_data))
    # print(json.loads(request.body)['name'])
    # form = ProductForm(instance=object)
    # old_data={'name': 'electric jeep', 'price': 1000000.0, 'discount': 50000.0}
    form = ProductForm(old_data,instance=obj)
    print(form)
    # print(form.is_valid())
    if form.is_valid():
        form.save()
        return HttpResponse("Updated field value successfully...")
    
@csrf_exempt
def update(request,id):
    object=Product.objects.get(id=id)
    print(type(request.body))
    print(request.body)
    # print(json.loads(request.body))
    # print(json.dumps(request.body))
    print(request.POST)
    # object.update(request.body)
    form = ProductForm(instance=object)
    # print(form)
    # print(request.POST == 'POST')
    # if request.method == 'PUT':
    print(json.loads(request.body))
    print(type(json.loads(request.body)))
    form=ProductForm(json.loads(request.body),instance=object)
    print(form)
    if form.is_valid:
        form.save()
        return HttpResponse('data updated successfully...')
    else:
        return render(request,'crud_app/update.html',{'form':form})
@csrf_exempt 
def delete(request,id):   
        Product.objects.get(id=id).delete()
        return HttpResponse("Record deleted successfully...")