from django.contrib import admin
from django.urls import path
from . import views
#from portfolio import views
#from django . conf . urls . static import static
#from django.conf import settings
app_name='blog'
urlpatterns = [
    path('', views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/', views.detail,name='detail'),
    
   
]