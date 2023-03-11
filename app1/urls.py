from django.urls import path
from app1.views import *


urlpatterns = [
    path("sample1/",sample1,name="sample")
]