from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name= 'index'),
    path('about', views.about, name= 'about'),
    # path('blog', views.blog, name= 'blog'),
    path('coffees', views.coffees, name= 'coffees'),
    # path('contact', views.contact, name= 'contact'),
]