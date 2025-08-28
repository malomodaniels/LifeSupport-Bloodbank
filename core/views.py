from django.shortcuts import render, redirect
from .models import Donor, Recipient
from .forms import DonorForm, RecipientForm

from django.shortcuts import render
from .models import Donor, Recipient

def index(request):
    # Explicit ordering
    donors = Donor.objects.order_by('name')          # alphabetical
    recipients = Recipient.objects.order_by('-urgency')  # highest urgency first

    context = {
        "donors": donors,
        "recipients": recipients
    }

    response = render(request, "/index.html", context)
    response['Content-Type'] = "text/html"
    return response

def add_donor(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DonorForm()
    return render(request, "add_donor.html", {"form": form})


def add_recipient(request):
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RecipientForm()
    return render(request, "add_recipient.html", {"form": form})

from django.http import HttpResponse

def test_view(request):
    html_content = "<h1>Hello Django!</h1>"
    return HttpResponse(html_content, content_type="text/html")
