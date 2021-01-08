from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginate, name='paginate')
    ]
