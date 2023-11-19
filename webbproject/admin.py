from django.contrib import admin
from .models import experience,education, projects, category

# Register your models here.
admin.site.register(experience)
admin.site.register(education)
admin.site.register(projects)
admin.site.register(category)

