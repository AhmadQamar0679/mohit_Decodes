from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Contact

# Create your views here.
def contact(request):
    all_messages=Contact.objects.all()
    return render(request,'contact.html',{'all_messages':all_messages})


def submit(request):
    if request.method=='POST':
        name=request.POST.get('name')
        message=request.POST.get('message')
        if name and message:
            Contact.objects.create(name=name,message=message)
            return HttpResponse(f'Thank you,{name}, for this message!')
        else:
            HttpResponse('Please Provide both name message.')
        

    return redirect('contact.html')



    # return render (request,'submit.html')