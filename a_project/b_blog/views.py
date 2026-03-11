from django.shortcuts import render
from django.http import HttpResponse
from datetime  import datetime

# Create your views here.


class User:
    def __int__(self,name,age):
        self.name=name
        self.age=age

def  home(request):
    context={
        'name':"Ahmad Qamar",
        'age':21,
        'skill':['Django','Python','FastApi','React'],
        'user':User('Ahmad Qamar',21),
        'blog':{
            'title':'Django Templates intro',
            'content':'<b>Welcom to django Templates</b>',
            'created at':datetime(2026,3,11,12,30 )
        },
        'empty_value':None

    }
    return render(request,f'home.html',context)



def about(request):
    return render(request,'about.html')
