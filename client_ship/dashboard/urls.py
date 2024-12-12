from django.urls import path 
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard') #map the root URL of the app to the view
] 