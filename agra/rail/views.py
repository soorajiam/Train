from django.views import generic
from .models import User,Train,Station,Tinfo
#from .models import Product,Purchase,Plist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

# Create your views here.
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def registerp(request):
    email=request.POST.get("email","")
    name=request.POST.get("name","")
    gender=request.POST.get("gender","")
    mobile=request.POST.get("mobile","")
    city=request.POST.get("city","")
    state=request.POST.get("state","")
    username=request.POST.get("username","")
    password=request.POST.get("password","")
    users=User.objects.all().filter(email_id=email)
    got=0
    for u in users:
        got=1
    if (got==0):
        p=User(email_id=email,fullname=name,gender=gender,mobile=mobile,city=city,state=state,username=username,password=password)
        p.save()
        return HttpResponseRedirect('/rail/login')

    return render(request,'register.html')

def index(request):
    t=Train.objects.all()
    s=Station.objects.all()
    i=Tinfo.objects.all()

    return render(request, 'rail/index_admin.html',{'t': t ,'s':s,'i':i})

def trainDetail(request,pk):
    t=Train.objects.all().filter(trno=pk)
    s=Station.objects.all()
    i=Tinfo.objects.all()

    return render(request, 'rail/adminTrain.html',{'t': t ,'s':s,'i':i})

def searchsp(request):

    se='tripunitura'
    se=request.POST.get("search","")

    t=Train.objects.all()
    s=Station.objects.all().filter(Stname=se)
    i=Tinfo.objects.all()

    return render(request, 'rail/ssearch.html',{'t': t ,'s':s,'i':i,'se':se})




def bws(request):
    se=0

    t=Train.objects.all().filter(trno=se)
    s=Station.objects.all()
    i=Tinfo.objects.all()

    return render(request, 'rail/bws.html',{'t': t ,'s':s,'i':i,'se':se})

def bwsProcess(request):

    se='tripunitura'
    se1='tripunitura'
    se1=request.POST.get("search","")
    se=request.POST.get("search1","")

    t=Train.objects.all()
    s=Station.objects.all().filter(Stname=se)
    s1=Station.objects.all().filter(Stname=se1)
    i=Tinfo.objects.all()

    return render(request, 'rail/bws.html',{'t': t ,'s':s,'s1':s1,'i':i,'se':se})




def searchs(request):
    se=0

    t=Train.objects.all().filter(trno=se)
    s=Station.objects.all()
    i=Tinfo.objects.all()

    return render(request, 'rail/ssearch.html',{'t': t ,'s':s,'i':i,'se':se})

def searchtp(request):

    se=12512
    se=request.POST.get("search","")
    int(se)

    t=Train.objects.all().filter(trno=se)
    s=Station.objects.all()
    i=Tinfo.objects.all()

    return render(request, 'rail/tsearch.html',{'t': t ,'s':s,'i':i,'se':se})




def searcht(request):
    se=0

    t=Train.objects.all().filter(trno=se)
    s=Station.objects.all()
    i=Tinfo.objects.all()

    return render(request, 'rail/tsearch.html',{'t': t ,'s':s,'i':i,'se':se})



def loginp(request):
    uname=request.POST.get("username","")
    pword=request.POST.get("password","")
    u=User()
    if(len(uname) == 0 and len(pword) == 0):
        return render(request,'login.html')
    userd=User.objects.all().filter(username=uname)
    for u in userd:
        a=0
    if (u.password==pword):
        request.session['logid'] = username
        return HttpResponseRedirect('/rail')
    else:
        return render(request,'login.html')

    return render(request,'register.html')


class trainCreate (CreateView):
    model=Train
    fields=['trno','trname']

class trainUpdate (UpdateView):
    model=Train
    fields=['trno','trname']

class trainDelete (DeleteView):
    model=Train
    success_url='/rail'

class DetailView(generic.DetailView):

    model=Train
    template_name='rail/detail.html'


class stCreate (CreateView):
    model=Station
    fields=['stationC','Stname']

class stUpdate (UpdateView):
    model=Station
    fields=['stationC','Stname']

class stDelete (DeleteView):
    model=Station
    success_url='/rail'

class stView(generic.DetailView):

    model=Station
    template_name='rail/sdetail.html'
class dCreate (CreateView):
    model=Tinfo
    fields=['trno','pid','ordn0','stationC','sA','aD','A','D','late']

class dUpdate (UpdateView):
    model=Tinfo
    fields=['trno','pid','ordn0','stationC','sA','aD','A','D','late']

class dDelete (DeleteView):
    model=Tinfo
    success_url='/rail/admin'

class dView(generic.DetailView):

    model=Tinfo
    template_name='rail/ddetail.html'
