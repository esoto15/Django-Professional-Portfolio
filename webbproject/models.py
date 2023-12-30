from django.db import models
from django.urls import reverse

# Create your models here.
class experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    description = models.TextField()
    

class education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    description = models.TextField()
    gpa = models.CharField(max_length=100)
    honors = models.TextField()
    

class category(models.Model):
    name = models.CharField(max_length=100)
    
    
class projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    skills = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

class Language(models.Model):
    # Name of the language, e.g., English, Spanish, etc.
    name = models.CharField(max_length=100)

    # Category of the language, e.g., Programming, Natural, etc.
    category = models.CharField(max_length=100)

    # Image field to store the logo image
    logo = models.ImageField(upload_to='language_logos/', null=True, blank=True)

    def __str__(self):
        return self.name
    
 
#  Instructions for running the server
# Create class
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# views.py  -  add class to index
# admin.py  -  register class
