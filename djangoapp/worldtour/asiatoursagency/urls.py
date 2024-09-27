from django.urls import path
from . import views # The . means from the current directory import views.

urlpatterns = [
    path('',views.index)
]

