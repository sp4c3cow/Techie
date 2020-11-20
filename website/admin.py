from django.contrib import admin
from .models import ContactForm

class AdminContactForm(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'date']

admin.site.register(ContactForm, AdminContactForm)
