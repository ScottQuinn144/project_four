from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/', views.CustomerForm.as_view(), name='book'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu')

]
