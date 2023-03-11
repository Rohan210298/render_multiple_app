from django.urls import path
from app2.views import *

urlpatterns = [
    path("sample2/",sample2,name="sample2")
]