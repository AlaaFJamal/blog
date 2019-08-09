from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
	my_title = "Home"
	context = {
		"title": my_title		
	}
	if request.user.is_authenticated:
		context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
	return render(request, "home.html", context)

def about_page(request):
	context = {
		"title": "About Us"
	}
	return render(request, "about.html", context)

def contact_page(request):
	context = {
		"title": "Contact Us"
	}
	return render(request, "contact.html", context)