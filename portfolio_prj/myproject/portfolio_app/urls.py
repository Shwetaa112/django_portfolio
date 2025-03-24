from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('certificate/',views.certificate,name='certificate'),
    path('resume_list/', views.resume_list, name='resume_list'),
    path('certificate/delete/<int:cert_id>/', views.delete_certificate, name='delete_certificate'),



]