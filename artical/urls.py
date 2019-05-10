from django.urls import path
from . import views

app_name='artical'
urlpatterns=[
    path('',views.index,name='index'),
    path('<int:artical_id>/',views.artical,name='artical_id'),
    path('<str:slug>/',views.artical,name='slug'),

]