from . import views
from django.urls import path

urlpatterns = [
    path('about/',views.about,name='about'),
    path('condact/',views.contact,name='contact'),
    path('details/', views.details, name='details'),
    path('home/', views.home, name='home'),
    path('tanks/', views.tanks, name='tanks'),
    path('add/', views.add, name='add'),
    path('res/',views.result,name='result'),
    path('',views.index,name='index'),





]

