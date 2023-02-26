"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def view_add(request,a,b):#request or any name
    result=a+b
    res=HttpResponse("<h1>Hello I am Calling Summation of Two Number</h1>"+str(result))
    return res

def view_sub(request):
    res=HttpResponse("<h1>Hello I am Calling Subtraction of Two Number</h1>")
    return res

def view_calc(request):
    a=int(request.POST.get('val1',0))
    b=int(request.POST.get('val2',0))
    if request.method=="GET":
        return render(request,'calc.html')
    elif request.method=="POST":
        if 'btnsum' in request.POST:
            # a=int(request.POST.get('val1',0))
            # b=int(request.POST.get('val2',0))
            res=a+b
            # d1={'a':a,'b':b,'res':res}
            # return render(request,'calc.html',context=d1)
        elif 'btnsub' in request.POST:
            # a=int(request.POST.get('val1',0))
            # b=int(request.POST.get('val2',0))
            res=a-b
            # d1={'a':a,'b':b,'res':res}
            # return render(request,'calc.html',context=d1)
        elif 'btnmul' in request.POST:
            # a=int(request.POST.get('val1',0))
            # b=int(request.POST.get('val2',0))
            res=a*b
            # d1={'a':a,'b':b,'res':res}
            # return render(request,'calc.html',context=d1)
        elif 'btndiv' in request.POST:
            # a=int(request.POST.get('val1',0))
            # b=int(request.POST.get('val2',0))
            res=a/b
            # d1={'a':a,'b':b,'res':res}
            # return render(request,'calc.html',context=d1)
        d1={'a':a,'b':b,'res':res}
        return render(request,'calc.html',context=d1)
    
    # a=int(request.POST.get('val1',0))
    # b=int(request.POST.get('val2',0))
    # res=a+b
    # d1={'a':a,'b':b,'res':res}
    # return render(request,'calc.html',context=d1)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/<int:a>/<int:b>/',view_add),
    path('sub/',view_sub),
    path('calc/',view_calc),
]
