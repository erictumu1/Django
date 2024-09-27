from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

#This is the homepage view function.
def home_view(request):
    return render(request, 'form_app/home.html')

#This is to define the contact_view function to handle the contact form.
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form':form} #context is always a dictionary.
    return render(request, 'form_app/contact.html',context)

#Defining the contact_success_view function to handle the success.
def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')  