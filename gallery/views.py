from django.shortcuts import render
from .models import *
# Create your views here.
def gallery(request):
	cats=Category.objects.all()
	images=Image.objects.all()
	data={'images':images, 'cats':cats}


	return render(request,"gallery.html",data)

def show_category_page(request,cid):
	cats=Category.objects.all()
	category=Category.objects.get(pk=cid)
	images=Image.objects.filter(cat=category)
	data={'images':images, 'cats':cats}


	return render(request,"gallery.html",data)




