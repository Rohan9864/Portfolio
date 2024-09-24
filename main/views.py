from django.shortcuts import render,redirect
from .models import Contact,Projects
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
# Create your views here.
def index(request):
    date=datetime.now().year
    data=Projects.objects.all()
    return render(request, 'index.html',{'data':data,'date':date})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date=datetime.now()

        Contact.objects.create(name=name,email=email,phone=phone,message=message)

        subject='Contact Request'
        message=render_to_string('msg.html',{'name':name,'date':date})
        from_email='dahalrohan82@gmail.com'
        recipient_list=[email]
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)

    return render(request,'index.html')

