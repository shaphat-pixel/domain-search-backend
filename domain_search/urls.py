
from django.contrib import admin
from django.urls import path
from scraper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name-cheap/', views.NameCheap, name='post'),
    path('domain/', views.Domain, name='post'),
    path('hover/', views.Hover, name='post')
]
