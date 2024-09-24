from django.contrib import admin
from .models import Contact,Projects
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email','phone','message']

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'url', 'github','photo']