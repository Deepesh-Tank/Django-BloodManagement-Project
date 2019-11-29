from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import NeedBlood
from .models import DonateBlood
from .models import Blood_Bank
from .models import fact
from .models import Blood_Camps
from .models import chart
import re


def index(request):
    return render(request,'index.html')
def index1(request):
    return render(request,'index1.html')
def index2(request):
    return render(request,'index2.html')
def sing(request):
    return render(request,'sing.html')
def facts(request):
    a=fact.objects.all()
    return render(request,'facts.html',{'a':a})

def chart1(request):
    a=chart.objects.all()
    return render(request,'chart1.html',{'a':a})

def test(request):
    a=Blood_Bank.objects.all()
    return render(request,'test.html',{'a':a})
def test1(request):
    a=Blood_Camps.objects.all()
    return render(request,'test1.html',{'a':a})
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        ff=0
        while True:   
            if not re.search("[@]", email): 
                messages.info(request,'Not a valid Email-id')
                ff=-1
                return redirect('register')
                break
            else:
                ff=0
                break
        
        password = password1
        flag = 0
        while True:   
            if (len(password)<8): 
                flag = -1
                messages.info(request,'Password length must be at least 8 characters.NOTE: Password must contain at least one capital alphabet,special character and numeric digit.')
                return redirect('register')
                break
            elif not re.search("[A-Z]", password): 
                flag = -1
                messages.info(request,'Password must contain atleast one capital alphabet.NOTE:Password must contain at least one capital alphabet,special character and numeric digit.')
                return redirect('register')
                break
            elif not re.search("[0-9]", password): 
                flag = -1
                messages.info(request,'Password must contain atleast one numeric digit. NOTE:Password must contain at least one capital alphabet,special character and numeric digit.')
                return redirect('register')
                break
            elif not re.search("[!@#$%^&*()_]", password): 
                flag = -1
                messages.info(request,'Password must contain atleast one special character.Password must contain at least one capital alphabet,special character and numeric digit.')
                return redirect('register')
                break
            elif re.search("\s", password): 
                flag = -1
                break
            else: 
                flag = 0
                break
  
    
   

        if password1==password2 and flag == 0 and ff==0:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1 , email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("usr don")
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def need(request):
    print('form submitted')
    city=request.POST['city']
    requestname=request.POST['requestname']
    contact=request.POST['contact']
    blood_group=request.POST['blood_group']

    needer = NeedBlood(blood_group=blood_group,requestname=requestname,city=city,contact=contact)
    needer.save();
    return render(request,'index.html')

def donate(request):
    print('form submitted')
    city=request.POST['city']
    donorname=request.POST['donorname']
    contact=request.POST['contact']
    blood_group=request.POST['blood_group']

    needer = DonateBlood(blood_group=blood_group,donorname=donorname,city=city,contact=contact)
    needer.save();
    return render(request,'index.html')

def temp(request):
    a=DonateBlood.objects.filter.all()
    return render(request,'temp.html',{'a':a})

def requestlist(request):
    return render(request,'requestlist.html')
def donorlist(request):
    return render(request,'donorlist.html',)


def don(request):
    c=request.POST['blood_group']
    b=request.POST['city']
    a=DonateBlood.objects.filter(blood_group=c,city=b)
    return render(request,'donorlist.html',{'a':a})

def req(request):
    c=request.POST['blood_group']
    b=request.POST['city']
    a=NeedBlood.objects.filter(blood_group=c,city=b)
    return render(request,'requestlist.html',{'a':a})

def dlist(request):
    return render(request,'dlist.html')

def rlist(request):
    return render(request,'rlist.html')

def check(request):
    return render(request,'check.html')