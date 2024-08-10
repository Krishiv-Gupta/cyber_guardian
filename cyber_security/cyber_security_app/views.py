from django.shortcuts import render, redirect
from .models import e,SafetyTest,sign


# Create your views here.
def home(requests):
    return render(requests, 'home.html')

def play(request):
    return render(request,"knowledge.html")

def test(request):
    return render(request,"test.html")

def safe(request):
    if request.method=="POST":
        a=request.POST['opt0']
        
        print(a)
        
    return render(request,"test.html")

def send(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        w=request.POST['reason']

        b=e(Name=name,Email=email,Phone=phone,W=w)
        b.save()

        return redirect('home')
    return render(request,"home.html")

def signup(request):
    return render(request, "signup.html")

def sign1(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
    

        c=sign(email=email, Password=password)
        c.save()

        return redirect('home')
    return render(request,"home.html")
