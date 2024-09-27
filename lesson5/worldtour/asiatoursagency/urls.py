from django.urls import path
from . import views

urlpatterns = [
   path('', views.index), #If you miss the comma, it breaks the whole code.
]
