from django.urls import path
from .views import index,contact,Projects

urlpatterns = [
    path("",index,name="index"),
    path('contact/',contact,name='contact'),
    path("project/",Projects,name='project')
]
