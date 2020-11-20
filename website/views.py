from django.shortcuts import render

from website.models import ContactForm


def index(request):
    return render(request, 'html/index.html')

def contact_form(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = ContactForm(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()
        return render(request, 'html/success.html')
    else:
        return render(request, 'html/index.html')