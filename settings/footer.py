from .models import Info , Services

def myfooter(request):
    myfooter = Info.objects.last()
    service = Services.objects.all()
    context = {
        'myfooter':myfooter , 
        'service':service ,
    }
    return context