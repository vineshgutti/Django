from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def crate(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
        else:
            form = ProductForm()
    else:
        return render(request, 'crud_app/form.html', {'form':form})
    
def details(request):
    data = Product.objects.all()
    return render(request, 'crud_app/details.html', {'data':data})

def update(request,id):
    object=Product.objects.get(id=id)
    form = ProductForm(instance=object)
    if request.method == 'POST':
        form=ProductForm(request.POST,instance=object)
        print(form)
        if form.is_valid:
            form.save()
            return redirect('details')
    else:
        return render(request,'crud_app/update.html',{'form':form})
    
def delete(request,id):   
        Product.objects.get(id=id).delete()
        return redirect('details')
    
