from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"FUCK YOU",
        "variable2":"FUCK ASSHOLE"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact= Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'complante has been registard.')
    return render(request, 'contact.html')    
    #return HttpResponse("this is phone page")
