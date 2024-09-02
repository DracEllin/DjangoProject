from django.shortcuts import render
from django.contrib.auth.views import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'