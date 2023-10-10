from .models import Info , Services

def myfooter(request):
    myfooter = Info.objects.last()
    service_footer = Services.objects.all()[:4]
    context = {
        'myfooter':myfooter , 
        'service_footer':service_footer ,
    }
    return context