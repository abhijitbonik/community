from django.shortcuts import render, redirect
from .forms import NewArticleForm
from django.http import Http404, HttpResponse
from .models import Articles

# Create your views here.

def home(request):
	articles=Articles.objects.all()
	return render(request, 'home.html',{'articles':articles})

def newArticle(request):
	if request.method == 'POST':
		form = NewArticleForm(request.POST)
		if form.is_valid():
			obj = Articles.objects.create(
				title = form.cleaned_data.get('title'),
				body  = form.cleaned_data.get('body')
				)
			articles=Articles.objects.all()
			return render(request, 'home.html',{'articles':articles})

	return render(request, 'new_article.html')

