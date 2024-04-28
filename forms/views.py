from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.core.mail import send_mail
from .models import NameForm, Contact

# Create your views here.

def get_name(req: HttpRequest):
    if req.method == "POST":
        form = NameForm(req.POST)
        if form.is_valid:
            print(form.cleaned_data)
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()
    return render(req, "name.html", {"form":form})

def contact(req: HttpRequest):
    if req.method == "POST":
        form = Contact(req.POST)
        
        if form.is_valid:
            data = form.cleaned_data
            subject = data["subject"]
            message = data["message"]
            sender = data["sender"]
            receivers = ["info@example.com"]
            if data["cc_myself"]:
                receivers.append(sender)
            send_mail(subject, message, sender, receivers)
            print(data)
            return HttpResponseRedirect("/thanks/")
    else:
        form = Contact()
    return render(req, "contact.html", {"form": form})