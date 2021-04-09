from functools import lru_cache
from django.shortcuts import render
from .forms import CreateContactForm
from .models import ContactUs
from eshop_settings.models import SiteSetting


@lru_cache
def contact_us(request):
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        message = contact_form.cleaned_data.get('message')
        ContactUs.objects.create(name=full_name, email=email, subject=subject, message=message, is_read=False)
        contact_form = CreateContactForm()
    settings = SiteSetting.objects.first()
    context = {'form': contact_form, 'settings': settings}
    return render(request, 'contact-us/contact_us.html', context)
