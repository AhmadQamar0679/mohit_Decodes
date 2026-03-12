from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.home,name='home_page'),
    path('about/',views.about,name='about_page'),
    path('blog/',views.blog_detail,name='blog_page')

   

    ]
