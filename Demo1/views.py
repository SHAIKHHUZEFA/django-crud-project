from django.shortcuts import redirect,render
from .import models,myform
from django.http import HttpResponse

# Create your views here.
def first(request):
    product=models.Product.objects.all()
    return render(request,"/Users/Huzefa/PycharmProjects/djangocrudpro/Testing/templates/test1.html",{'products':product})

def create(request):
    if request.method=="POST":
        form=myform.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("first")
    else:
        form=myform.ProductForm()
    return render(request,"/Users/Huzefa/PycharmProjects/djangocrudpro/Testing/templates/test2.html",{'pform':form})

def update(request, id):
    product = models.Product.objects.get(id=id)
    form = myform.ProductForm(initial= {
        "pname":product.pname,
        "pprice":product.pprice,
        "pquantity":product.pquantity
    })
    return render(request,"/Users/Huzefa/PycharmProjects/djangocrudpro/Testing/templates/test3.html",{'pform':form,'id':id})

def save_product(request):
    if request.method=="POST":
        id=request.POST.get("id")
        product = models.Product.objects.get(id=id)
        form = myform.ProductForm(request.POST)
        if form.is_valid():
            form=myform.ProductForm(request.POST, instance=product)
            form.save()
            return redirect("first")
        else:
           return HttpResponse("there was a error during updation")

def delete(request,id):
    product = models.Product.objects.get(id=id)
    product.delete()
    return redirect("first")












