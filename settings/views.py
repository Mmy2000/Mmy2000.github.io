from django.shortcuts import render
from .models import About , Resume , Services
from projects.models import Projects
from django.db.models import Count

# Create your views here.

def home(request):
    about = About.objects.last()
    project_count = Projects.objects.all().count() 
    resume = Resume.objects.all()
    service = Services.objects.all()



    return render(request,'home.html', {
        'about':about  , 
        'project_count':project_count,
        'resume':resume ,
        'service':service,
    })