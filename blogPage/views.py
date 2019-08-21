from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import BlogPost
from .forms import ContactForm
from .forms import BlogPostForm
from .forms import BlogPostModelForm

from django.http import Http404

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
	#print(request.POST)
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()

	context = {
		"title": "Contact Us",
		"form": form
	}

	return render(request, "contact.html", context)

# GET -> 1 object
# filter -> [] of objects

# def blog_post_detail_page(request, slug):
# 	#print("Django says: Method is ", request.method, "Path is: ", request.path, "User: ", request.user)
# 	queryset = BlogPost.objects.filter(slug=slug) #query -> database -> data -> django renders it
# 	if queryset.count() == 0:
# 		raise Http404
# 	obj = queryset.first()		
# 	#obj = filter_object_or_404(BlogPost, slug=slug)
		
# 	template_name = 'blog_post_detail.html'
# 	context = {"object": obj} # {"title": obj.title}
# 	return render(request, template_name, context)

# CRUD Create Retrieve Update Delete

# GET -> Retrieve / List

# POST -> Create / Update / DELETE

def blog_post_list_view(request):
	# list out objects
	# could be search
	qs = BlogPost.objects.all() # queryset -> list of python objects
	#qs = BlogPost.objects.filter(title__icontains='python') # in search
	template_name = 'blog_post_list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)

#@login_required
@staff_member_required
def blog_post_create_view(request):
	# create objects
	# ? use a form

	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = BlogPostModelForm()
		
		
	template_name = 'blog_post_create.html'
	context = {'form': form}
	return render(request, template_name, context)

def blog_post_detail_view(request, slug):
	# 1 object -> detail view
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog_post_detail.html'
	context = {'object': obj}
	return render(request, template_name, context)

def blog_post_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog_post_update.html'
	context = {'object': obj, 'form': ''}
	return render(request, template_name, context)

def blog_post_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog_post_delete.html'
	context = {'object': obj}
	return render(request, template_name, context)



