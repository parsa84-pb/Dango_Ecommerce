from django.contrib import admin
from .models import SiteSetting


# Register your models here.

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['__str__', "siteAddress", 'sitePhone', 'siteMobile', 'siteEmail', 'siteFax']

    class Meta:
        model = SiteSetting


admin.site.register(SiteSetting, SiteSettingsAdmin)
