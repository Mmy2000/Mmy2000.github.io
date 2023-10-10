from django.urls import path
from . import views

app_name = 'settings'

urlpatterns = [
    path( '',views.home , name='home' ),   
    path( 'service',views.ServiceList.as_view() , name='service_list' ),     
    path( '<slug:slug>',views.ServiceDetail.as_view() , name='service_detail' ),  
    path('category/<str:slug>' , views.ServiceByCategory.as_view() , name='service_by_category'),   
]