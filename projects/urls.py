from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('' , views.ProjectList.as_view() , name='projects_list'),
    #path('<slug:slug>' , views.ProjectDetail.as_view() , name='post_detail'),
    #path('category/<str:slug>' , views.PostByCategory.as_view() , name='post_by_category'),
    #path('tags/<str:slug>' , views.PostByTags.as_view() , name='post_by_tags'),
]