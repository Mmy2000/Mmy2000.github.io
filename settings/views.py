from django.shortcuts import render
from .models import About 
from projects.models import Projects
# Create your views here.

def home(request):
    about = About.objects.last()
    project_count = Projects.objects.filter().count() ,



    return render(request,'home.html', {
        'about':about  , 
        'project_count':project_count,
    })