from django.contrib import admin
from django.urls import path, re_path
from adoptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    re_path(r'^/adoptions/(?:page-(?P<page_number>\d+)/)?$', views.pet_detail),
]
