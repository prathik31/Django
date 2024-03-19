# user--- todolist       pass---- 123456


from django.shortcuts import render,HttpResponse,redirect
from .models import task
from .forms import *
# Create your views here.
def index(request):

    TASKS=task.objects.all()

    FORM=taskform()
    
    if request.method=='POST':
        form = taskform(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    
    context={'task':TASKS,'form':FORM}
    return render(request,'index.html',context)

def update(request,id):
    TASKS=task.objects.get(id=id)
    form =taskform(instance=TASKS)
    
    if request.method=='POST':
        form = taskform(request.POST,instance=TASKS)
        if form.is_valid:
            form.save()
            return redirect('/')
    context={'form':form}

    return render(request,'update.html',context)

def delete(request,id):
    TASKS=task.objects.get(id=id)
    TASKS.delete()
    return redirect('/')