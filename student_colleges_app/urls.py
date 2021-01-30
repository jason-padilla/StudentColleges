from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add-student', views.add_student),	   
    path('add-college', views.add_college),	 
]