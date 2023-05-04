from django.shortcuts import render,HttpResponseRedirect
from.forms import studentregistration
from .models import user

def add_show(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            reg.save()
            fm = studentregistration()
    else:
        fm = studentregistration()
    stud = user.objects.all()
    return render(request,'enroll/addandshow.html', {'form':fm,'stu':stud})

def update_data(request,id):
    if request.method == 'POST':
        pi=user.objects.get(pk=id)
        fm=studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
     pi=user.objects.get(pk=id)
     fm=studentregistration(instance=pi)         
    return render(request,'enroll/update.html',{'form':fm})



def delete_data(request,id):
    if request.method == 'POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')