from django.shortcuts import render, get_object_or_404,redirect
from clothing.models import product
from .forms import Productform
# Create your views here.
def clothing(request):
    form=Productform()
    pro_img=product.objects.all()
    
    if request.method == "POST":
        form= Productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form= Productform()
            
    return render(request,'clothing/fashion.html',{'pro_img':pro_img,'form':form})



def edit_product(request,product_id):
    Product= get_object_or_404(product, id=product_id)
    
    if request.method == "POST":
        form= Productform(request.POST, request.FILES,instance=Product)
        if form.is_valid():
            form.save()
            return redirect('clothing')
    
    else:
        form= Productform(instance=Product)
            
    return render(request,'clothing/edit_product.html',{'form':form})

def delete_product(request,product_id):
    Product= get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        Product.delete()
        return redirect('clothing')
            
    return render(request,'clothing/confirm_delete.html',{'product':product})