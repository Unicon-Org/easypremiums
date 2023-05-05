import sys
sys.path.append("easypremiums")

from django.shortcuts import render
from constants import SUBSCRIPTIONS

from .models import Faq

# Create your views here.
def home_page(request):
    # Home
    return render(request, 'index.html', {'subs': SUBSCRIPTIONS})

def about(request):
    # Faq
    all_faqs = Faq.objects.all()
    return render(request, 'about.html', {'faqs': all_faqs})

def blog(request):
    return render(request, 'blog.html')

def coffees(request):
    # Purchase
    return render(request, 'coffees.html', {'subs': SUBSCRIPTIONS})

def contact(request):
    return render(request, 'contact.html')