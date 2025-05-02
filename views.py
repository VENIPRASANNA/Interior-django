from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# myapp/views.py

def index(request):
    return render(request, 'myapp/index.html')

def login(request):
    return render(request,'myapp/login.html')

def design(request):
    return render(request,'myapp/design.html')

def contact(request):
    return render(request,'myapp/contact.html')

def int1(request):
    return render(request,'myapp/int1.html')

def int2(request):
    return render(request,'myapp/int2.html')

def order(request):
    return render(request,'myapp/order.html')

def project(request):
    return render(request,'myapp/project.html')

def recent(request):
    return render(request,'myapp/recent.html')

def req(request):
    return render(request,'myapp/req.html')

def offer(request):
    return render(request,'myapp/offer1.html')
# def home(request):
#     return HttpResponse("Welcome to My Website!")
