from django.shortcuts import render
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