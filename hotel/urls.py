from .views import RoomListView,BookingListView, RoomDetailView, CancelBookingView
from . import views
app_name = 'hotel'
from django.urls import path,include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('room_list_view/', RoomListView, name='RoomListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='CancelBookingView'),
   



]
