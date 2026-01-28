from django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
#     return HttpResponse("About")

def AboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")
def movies(request):
    return render(request,"movies.html")

def news(request):
    return render(request,"news.html")  

def shows(request):
    return render(request,"shows.html")

def recipe(request):
    ing = ["maggie","tomato"]
    data = {"name":"maggie","time":1,"ingredient":ing}
    return render(request,"recipe.html",data)

def team(request):
    team = ["salt","kohli","paddikal","rajat","jitesh","mayank","tim","romario","krunal","livingstone","suyansh","jacob"]
    rcb = {"name":"royal chalangers bangaluru","trophy":1,"team":team,"captain":"rajat patidar"}
    return render(request,"team.html",rcb)

def cars(request):
    car = ["bmw","audi","mercedece","porsche","mustang"]
    about = {"type":"sports","rating":9,"car":car}
    return render(request,"cars.html",about)