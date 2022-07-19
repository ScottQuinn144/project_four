from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/', views.MakeABooking, name='book'),
    path('booking/', views.MakeABook, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu')
]
