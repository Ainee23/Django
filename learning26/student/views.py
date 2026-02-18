from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .forms import ServiceForm
from services.models import Service


# Create your views here.
def login(request):
    return render(request, "student/login.html")

def marksheet(request):
    marks = {"maths": 80, "chemistry": 81, "physics": 90, "english":95}
    return render(request, "student/marksheet.html",marks)

def information(request):
    info = {"name":"abc", "age":23 , "city":"ahemdabad"}
    return render(request,"student/information.html",info)

def serviceList(request):
    services = Service.objects.all()
    return render(request,"student/serviceList.html",{"services":services})

def createService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createService.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"student/createService.html",{"form":form})
    
def deleteService(request, id):
    service = get_object_or_404(Service, id=id)

    service.delete()
    messages.success(request, "✅ Service deleted successfully.")
    return redirect("serviceList")