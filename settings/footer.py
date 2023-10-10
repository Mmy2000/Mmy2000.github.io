from .models import Info , Services , CategoryService
from django.db.models import Count
from django.views.generic import  ListView
from django.db.models.query_utils import Q



def myfooter(request):
    myfooter = Info.objects.last()
    categories_service = CategoryService.objects.all().annotate(service_count=Count('service_category'))[:4]
    context = {
        'myfooter':myfooter , 
        'categories_service' :categories_service,
    }
    return context

