from django.conf import settings
from django.shortcuts import render
from .models import About , Resume , Services
from projects.models import Projects
from blog.models import Post
from django.core.mail import send_mail

# Create your views here.

def home(request):
    about = About.objects.last()
    project_count = Projects.objects.all().count() 
    awards = project_count+2
    Cups_of_coffee = project_count*60
    resume = Resume.objects.all()
    service = Services.objects.all()
    recent_project = Projects.objects.all().order_by('-created_at')[:6]
    recent_blog = Post.objects.all().order_by('-created_at')[:3]




    return render(request,'home.html', {
        'about':about  , 
        'project_count':project_count,
        'resume':resume ,
        'service':service,
        'recent_project':recent_project,
        'recent_blog':recent_blog,
        'awards':awards,
        'Cups_of_coffee':Cups_of_coffee,
    })

def contact(request):
    if request.method == "POST":
        name = request.POST['your_name']
        email = request.POST['your_email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(['name'], ['email'], ['subject'],['message'], settings.EMAIL_HOST_USER)

        return render(request , 'contact.html' , {'name':name})
    else: 
        return render(request , 'contact.html' , {})