from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path("gallery", views.gallery, name="gallery"),
    path("category/<int:cid>/",views.show_category_page, name="category_page"),
    
   
    ]
