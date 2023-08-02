from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages


def index(request):
    context = {
        'variable': 'San'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    if(request.method == 'POST'):
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contactDetails = Contact(name=email, phone=phone, desc=desc, date=datetime.today())
        contactDetails.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contacts.html')
    # return HttpResponse('This is CONTACTS page')
