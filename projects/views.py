from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Projects , CategoryProject
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q



class ProjectList(ListView):
    model = Projects
    template_name = 'projects/project_list.html'
    paginate_by = 2
    def get_queryset(self) :
        name = self.request.GET.get('q','')
        object_list = Projects.objects.filter(
            Q(title__icontains = name) |
            Q(description__icontains = name)
        )
        return object_list