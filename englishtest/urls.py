from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('get_marks',views.get_marks,name='get_marks'),
    
]