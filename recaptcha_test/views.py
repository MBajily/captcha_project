from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('recaptcha_test:success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'recaptcha_test/contact_form.html', {'form': form})

def success(request):
    return render(request, 'recaptcha_test/success.html')