from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from .forms import RegisterForm,AluminiLoginForm
from .models import RegisterModel
from django.core.mail import send_mail,EmailMessage
from Notices.settings import EMAIL_HOST_USER
# Create your views here.

#converting passwords to hash value
import hashlib


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

'''def registerForm(request):
    if request.method =='POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")

    else :
        form = ContactForm()

    return render(request,'reg.html',{'form':form})

'''
'''def registerProcess(request):
    c = ContactModel(subject=request.POST['subject'],message=request.POST['message'],sender=request.POST['sender'],cc_myself=True)
    c.save()
    return HttpResponse(request.POST['subject'])'''

alumini_id=0

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'registerPage.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponse('thanks')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

def registerProcess(request):
    registrationNo = request.POST['registrationNo']
    username= request.POST['username']
    email = request.POST['email']
    password = encrypt_string(request.POST['password'])
    password_repeat = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    phone_number = request.POST['phone_number']
    degree = request.POST.get('degree',0)
    global alumini_id
    alumini_id+=1
    r = RegisterModel(registrationNo,email,username,password,password_repeat,first_name,last_name,phone_number,degree,False)
    try :
        r.save()
        send_mail('Alumnitracking', registrationNo+' You have Registered successfully wait untill your college admin verifies you.', EMAIL_HOST_USER, [email],fail_silently=False)
    except Exception as e:
        alumini_id-=1
        return HttpResponse("Error Error "+str(e))
    return redirect("main_page")

def alumini_login(request):
    template = 'alumini_login.html'
    if request.method=='POST':
        form=AluminiLoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('thanks')
        
    else :
        form = AluminiLoginForm()
    
    return render(request,template,{'form':form})
            

def loginProcess(request):
    username=request.POST['username']
    password=encrypt_string(request.POST['password'])
    #data = RegisterModel.objects.raw("select registrationNo,password_repeat from alumini_registermodel where registrationNo='"+username+"'")
    data=str(RegisterModel.objects.get(registrationNo=username)).split(" ")
    print(data)
    if data[0]==username and data[9]=='True':
        if data[3]==password:
            request.session['username'] = username
            print(data)
            return redirect('home_login')
        else:
            return HttpResponse("Your password is Incorrect!!!!")
    elif data[0]==username and data[9]=='False':
        return render(request,"notverified.html")
    else:
        return HttpResponse("Unexcepted Error!!!!!!!!!!!!!!")

def home_login(request):
    username=request.session.get('username', 'None')
    return render(request,'alumini.html',{'username':username})


def aluminiLogout(request):
    request.session['username'] = 0
    return redirect('main_page')


def sendingMail(request):

    #send_mail('Alumnitracking', 'Registered successfully', EMAIL_HOST_USER, ['aseefm25@gmail.com'], fail_silently=False)
    return HttpResponse("Sent Suceesfully")