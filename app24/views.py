from django.shortcuts import render
from .forms import ProductsForm
from .models import Products
# Create your views here.
def product_insert(request):
    context={}
    if request.method=='POST':
        form_obj=ProductsForm(request.POST or None,request.FILES or None)
        if form_obj.is_valid():
            form_obj.save()
            return render(request,"insert_result.html")

    else:
        form_obj=ProductsForm()
    context['form'] = form_obj
    return render(request,'input.html',context)

def display(request):
    data=Products.objects.all()
    return render(request,'display_result.html',{'records':data})