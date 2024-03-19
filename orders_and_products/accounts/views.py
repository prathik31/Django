from django.shortcuts import *
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login')
def index(request):
    CUSTOM=customer.objects.all()
    ORDE=order.objects.all()
    
    total_order=ORDE.count()
    total_delivered=ORDE.filter(status='delivered').count()
    total_pending=ORDE.filter(status='pending').count()

    contexts={'order':ORDE,'customer':CUSTOM,'total_order':total_order,'total_delivered':total_delivered,'total_pending':total_pending}
    return render(request,'dashboard.html',contexts)

def customers(request,id):                                     #the fun name should be diff from model name always. if it is same it gives error

    CUSTOM=customer.objects.get(id=id)
    ORDE=CUSTOM.order_set.all()
    total_order=ORDE.count()

    contexts={'customer':CUSTOM,'order':ORDE,'total_order':total_order}
    return render(request,'customer.html',contexts)

def product(request):

    product=products.objects.all()

    contexts={'prod':product}
    return render(request,'products.html', contexts)


def create_order(request):

    form=orderform()

    if request.method=='POST':
        form=orderform(request.POST)
        form.save() 
        return redirect('/')

    contexts={'form':form}
    return render(request,'create_form.html',contexts)


def update_order(request,id):

    ORDER=order.objects.get(id=id)
    form=orderform(instance=ORDER)

    if request.method=='POST':
        form=orderform(request.POST,instance=ORDER)
        form.save() 
        return redirect('/')

    contexts={'form':form,'order':ORDER}
    return render(request,'update_form.html',contexts)

def delete_order(request,id):
    ORDER=order.objects.get(id=id)
    ORDER.delete()
    return redirect('/')


def create_customer(request):

    form=customerform()

    if request.method=='POST':
        form=customerform(request.POST)
        if form.is_valid:
            form.save() 
            return redirect('/')

    contexts={'form':form}
    return render(request,'create_customer.html',contexts)

def update_customer(request,id):

    CUSTOM=customer.objects.get(id=id)
    form=customerform(instance=CUSTOM)

    if request.method=='POST':
        form=customerform(request.POST,instance=CUSTOM)
        form.save() 
        return redirect('/')

    contexts={'form':form,'customer':CUSTOM}
    return render(request,'update_customer.html',contexts)


def delete_customer(request,id):
    CUSTOM=customer.objects.get(id=id)
    CUSTOM.delete()
    return redirect('/')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"username/password is incorrect")
            return redirect('/login')
    return render(request,'login.html')


def logoutpage(request):
    logout(request)
    return redirect('/login')

def register(request):

    form=userform()
    if request.method=='POST':
        form=userform(request.POST)    
        form.save()
        messages.success(request,'account has successfully created')
        return redirect('/login')        
        
    contexts={'form':form}
    return render(request,'register.html',contexts)


def Add_product(request):
    form=productform()

    if request.method=='POST':
        form=productform(request.POST)
        if form.is_valid:
            form.save() 
            return redirect('/')

    contexts={'form':form}
    return render(request,'productform.html',contexts)