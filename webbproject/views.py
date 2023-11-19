from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import experience, education, projects, category

# Create your views here.
def index(response):
    return render(response, 'webapp/index.html', {'experiences': experience.objects.all(), 'educations': education.objects.all(), 'projects': projects.objects.all(), 'categories': category.objects.all()})
