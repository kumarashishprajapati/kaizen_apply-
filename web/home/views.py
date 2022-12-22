from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render

from home.models import apply



# Create your views here.

def home(request):
    return render(request,"index.html")
    # return HttpResponse("hi you are right")

def kaizen(request):
    if request.method == "POST":
        
        name=request.POST.get("name")
        department=request.POST.get("department")
        location=request.POST.get("location")
        details=request.POST.get("details")
        img1=request.POST.get("img1")
        img2=request.POST.get("img2")
        
        detail=apply(name=name,department=department,location=location,details=details,img1=img1,img2=img2,date=datetime.today())
        detail.save()
    return render(request,"kaizen.html")
def contact(request):
        return render(request,"contact.html")


