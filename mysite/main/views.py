from django.shortcuts import render, redirect
from . import models
from .forms import ContactModelForm
# Create your views here.


def home(request):
    car_list = models.Car.objects.all()
    return render(request, 'main/home.html', context={
        'car_list':car_list
    })


def about(request):
    info = models.About.objects.all()[0]
    return render(request, 'main/about.html', context={
        'info':info
    })


def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            models.Contact.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactModelForm()
    return render(request, 'main/contact.html', context={'form':form})