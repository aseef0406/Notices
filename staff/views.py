from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect

from alumini.models import RegisterModel
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def staffHome(request):
    return render(request, 'admin.html')


##################verification admin process######################


def verify(request):
    unverified_list = RegisterModel.objects.raw("select * from alumini_registermodel where verified=0")

    return render(request, 'verfication_of_alumini.html', {'unverified_list': unverified_list})


def verifyYes(request):
    registrationNo = request.POST['reg']
    # entry_list = RegisterModel.objects.get(registrationNo=registrationNo)
    # data = RegisterModel.objects.raw("select registrationNo,email,username,password,password_repeat,first_name,last_name,phone_number,degree from alumini_registermodel where registrationNo='Y16ACS496'")
    # print(entry_list)
    RegisterModel.objects.filter(registrationNo=registrationNo).update(verified=True)
    return HttpResponseRedirect("/staff/verification/")


def verifyNo(request):
    return HttpResponse( "In No method" + request.POST['reg'])

#############################################################################
'''def loginPage(request):
    return render(request, 'staff_login.html')

def loginPro(request):
    if request.method=="POST":
        username=request.POST['username']
        return HttpResponse(username)'''

def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)

            return redirect('staff_home')
        else:
            messages.info(request,'Username or password is incorrect')
            return render(request, 'staff_login.html')
    return render(request, 'staff_login.html')

def logoutPage(request):
    logout(request)
    return redirect('main_page')


