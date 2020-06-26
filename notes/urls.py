from django.urls import path, include
from notes.views import *

urlpatterns = [
    path('program/', program),
    path('course/', course)
]