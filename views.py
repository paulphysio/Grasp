
#from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Notify
from .forms import CreateNewList, NotificationForm


def Home(response):
    ls = ToDoList.objects.all()
    return render(response, "hello/Home.html", {"ls":ls})

def list(response):
    ls = ToDoList.objects.all()
    return render(response, "hello/list.html", {"ls":ls})
    
def boot(response):
    NotificationList = Notify.objects.all()
    context={
        "NotificationList": NotificationList
    }
    return render(response, "hello/boot.html", context)

def base(response):
    return render(response, "hello/base.html", {})

def create(request):
    print("working")
    form = CreateNewList(request.POST or None)
    if form.is_valid():
        print(form)
        form.save(commit=True)
    
        form = CreateNewList()
        return HttpResponseRedirect('/hello/list/')
    context = {
        'form':form
    } 
    return render(request, "hello/createlist.html", context)

def notify(request):
    form = NotificationForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = NotificationForm()
        return HttpResponseRedirect('/hello/boot/')
    context = {
        'form':form
    } 
    return render(request, "hello/notify.html", context)