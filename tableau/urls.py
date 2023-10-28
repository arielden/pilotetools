from django.urls import path
from . import views

app_name = 'tableau'

urlpatterns = [
    # tableau views
    path('', views.home, name='home'),
    
]

