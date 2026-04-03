from django.shortcuts import render

# Create your views here.
def student_detail(request):
    return render(request,'student_detail.html')
