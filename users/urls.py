from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
	path("", views.index, name="index"),
	path("index.html", views.index, name="index"),
	path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    path("profile", views.profile, name="profile"),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('reset_password/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
   
    ]
