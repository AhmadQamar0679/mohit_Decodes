from django.shortcuts import render
from django.http import HttpResponse
from datetime  import datetime

# Create your views here.


class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

def  home(request):
    context={
        'name':"Ahmad Qamar",
        'age':21,
        'skills':['Django','Python','FastApi','React'],
        'user':User('Ahmad Qamar',21),
        'blog':{
            'title':'Django Templates intro',
            'content':'Welcom to django Templates',
            'created_at':datetime.now
        },
        'empty_value':None

    }
    return render(request,'home.html',context)

 
# blog detail lecture 14


def blog_detail(request):
    post={
        'title':'This is post template render by blog page!',
        'description':"Django os high level Web language"

    }
    return render(request,'blog_detail.html',{'post':post})






def about(request):
    return render(request,'about.html')



# Lecture 15  templates


def blog_list(request):
    blogs=[
        {'title':'Hi my name is ahmad qamar and i am learning Advance Django'}

    ]
    context={
        "blogs":blogs

    }
    return render(request,'blog_list.html',context)