from django.shortcuts import render
from django.http import HttpResponse
from . models import Project, Imga
# Create your views hedjango
def home(request):
    project=Project.objects.all()
    #return HttpResponse("lol")
    return render(request,'portfolio/index.html',{'project':project})


def project(request):
    
    return render(request,'portfolio/project.html')





