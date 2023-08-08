from django.shortcuts import render,redirect
from app1.models import log,newuser
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def inser_home_dtls(request):
   if request.method == 'POST':
        data=User.objects.all()
        user_name=request.POST.get('un')
        password=request.POST.get('ps')  
        flag=0
        for da in data:
            if user_name==da.user_name and password==da.password:
               category1=da.user_type
               flag=1
               request.session['user_name']=user_name
               
               if category1=="dr":
                    return redirect('/new_user_dr')   
               elif category1=="ns":
                    return redirect('/new_user_nr')
               elif category1=="mngr":
                    return redirect('/new_user_mn')
               elif category1=="fronto":
                    return redirect('/new_user_off')
               elif category1=="sec":
                    return redirect('/new_user_sec')
               else:
                    return HttpResponse("invalid acct type")
        if flag==0:
            return HttpResponse("user does not exist") 
def new_user1(request):
     return render(request,'doctor.html')
def new_user2(request):
     return render(request,'nurse.html') 
def new_user3(request):
     return render(request,'mgmnt.html')
def new_user4(request):
     return render(request,'officer.html')
def new_user5(request):
     return render(request,'security.html')
    

def new_user_page(request):
    return render(request,'new_user.html')

def inser_new_user_dtls(request):
    y=User()
    y.username=request.POST.get('e')
    U
    password="qwerty"
    y.set_password(password)
    y.user_type=request.POST.get('jobrole')
    y.save()
    x=newuser()
    x.name=request.POST.get('n')
    x.job=request.POST.get('jobrole')
    x.join_date=request.POST.get('jn')
    x.email=request.POST.get('e')
    x.nobr=request.POST.get('pn')
    x.address=request.POST.get('add')
    x.save()
    return redirect('/new_user')



# Create your views here.
