from django.contrib import admin
from .models import ContactUs


# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__', "email", 'subject', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject', 'message']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactUsAdmin)
