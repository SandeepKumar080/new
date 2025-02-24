from django.shortcuts import render, HttpResponse
from.models import product
# Create your views here.
def home(request):
    prod= product.objects.all()
    return render(request,"electronics/home.html",{"prod":prod})
    