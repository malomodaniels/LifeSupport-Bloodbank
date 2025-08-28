# bloodbank/urls.py

from django.contrib import admin
from django.urls import path
from core.views import index, add_donor, add_recipient

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Landing page
    path('add-donor/', add_donor, name='add_donor'),
    path('add-recipient/', add_recipient, name='add_recipient'),
]
