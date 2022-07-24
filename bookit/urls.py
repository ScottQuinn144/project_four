from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/', views.MakeABooking, name='book'),
    path('contact/', views.ContactView, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu')
]
