from django.urls import path
from . import views


urlpatterns = [
    path('',views.contact,name='contact_page'),
    path('submit/',views.submit,name='submit_page')
]
