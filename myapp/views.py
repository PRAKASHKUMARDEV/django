from django.shortcuts import render
from .models import datas

# Create your views here.
def home (request):
    return render (request,"home.html")

def contact(request):
    if request.method=='get':
         name1=request.get['NAME']
         number1=request.get['NUMBER']
         email1=request.get['EMAIL']
         loc1=request.get['LOC']
         time1=request.get['TIME']

         obj=datas()
         obj.name=name1
         obj.number=number1
         obj.email=email1
         obj.location=loc1
         obj.time=time1
         obj.save()
         
         return render(request,'contact.html')  
    return render(request,'contact.html')