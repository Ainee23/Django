from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "student/login.html")

def marksheet(request):
    marks = {"maths": 80, "chemistry": 81, "physics": 90, "english":95}
    return render(request, "student/marksheet.html",marks)

def information(request):
    info = {"name":"abc", "age":23 , "city":"ahemdabad"}
    return render(request,"student/information.html",info)