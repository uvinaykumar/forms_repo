from django.shortcuts import render,redirect
from .forms import fromsform,loginform
from .models import formsmodel
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse

def home(request):
    show=formsmodel.objects.all()
    contex={'ashow':show}
    return render(request, 'home.html', contex)


def formsview(request):
    if request.method=="POST":
        eforms = fromsform(request.POST)
        if eforms.is_valid():
            name1=request.POST.get('name')
            email1=request.POST.get('email')
            sal1=request.POST.get('sal')
            loc1=request.POST.get('loc')
            mobile1=request.POST.get('mobile')
            username1=request.POST.get('username')
            password1=request.POST.get('password')

            data=formsmodel(
                name=name1,
                email=email1,
                sal=sal1,
                loc=loc1,
                mobile=mobile1,
                username=username1,
                password=password1,
            )
            data.save()
            return redirect('/')



    else:
        eforms = fromsform
        return render(request, '../../FullEcommerce/templates/forms/forms.html', {'abcd': eforms})


def loginview(request):
    if request.method=="POST":
        lform=loginform(request.POST)
        if lform.is_valid():
            user=request.POST.get('username')
            pwd=request.POST.get('password')

            user1=authenticate(username=user, password=pwd)

            if user1 is not None:
                login(request, user1)
                messages.warning(request,'Invalid username or Password')
                lform=loginform
                return render(request,'login.html',{'loform':lform})
            else:
                show=formsmodel.objects.all()
                contex={'ashow':show}
                messages.info(request,'successfully login')
                return render(request, 'home.html', contex)

    else:
        lform = loginform
        return render(request, 'login.html', {'loform': lform})

def LogoutUser(request):
    logout(request)
    return HttpResponse('successfully log out')



