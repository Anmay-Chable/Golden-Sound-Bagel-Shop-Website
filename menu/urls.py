from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'), # URL for the homepage of the bagel shop

]