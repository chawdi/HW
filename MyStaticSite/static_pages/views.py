from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import StaticPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.flatpages.models import FlatPage

def home(request):
    return render(request, 'static_pages/home.html')

def italic_page(request):
    return render(request, 'static_pages/italic_page.html')

def repeated_content_page(request):
    return render(request, 'static_pages/repeated_content_page.html')

def admin_only_page(request):
    return render(request, 'static_pages/admin_only_page.html')