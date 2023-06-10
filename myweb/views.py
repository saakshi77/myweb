from django.http import HttpResponse
from django.shortcuts import render


def homepg(request):
    data= {
        'title':'home new',
        'bdata':'welcome to MyWeb app',
        'clist':['PHP','java','django'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'pradeep','phone':9876543210},
            {'name':'upendra',"phone":1234567890}
        ]    
        }
    return render(request,'index.html',data)

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contact-us.html")

def packages(request):
    return render(request,"packages.html")
from django.shortcuts import render

def handle_404(request, exception):
    return render(request, '404.html', status=404)
