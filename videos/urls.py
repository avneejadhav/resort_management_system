from django.contrib import admin
from django.urls import path
from .views import CreateVideo, DetailVideo, UpdateVideo, DeleteVideo,VideoList

urlpatterns = [
	path('videos/', VideoList.as_view(), name='video'),
    path('create/', CreateVideo.as_view(), name='video-create'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='video-delete'),
   
]
