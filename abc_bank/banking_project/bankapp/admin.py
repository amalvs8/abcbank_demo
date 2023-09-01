from django.contrib import admin

from django.contrib import admin
from . models import District
from . models import Branch
from . models import Application

# Register your models here.

admin.site.register(District)
admin.site.register(Branch)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_no', 'gender', 'mail_id']
    list_editable = ['first_name', 'last_name']
    list_per_page = 20


admin.site.register(Application)

