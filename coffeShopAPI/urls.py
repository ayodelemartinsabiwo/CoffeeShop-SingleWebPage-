from django.urls import path
from . import views


urlpatterns = [
    # path('', Index.as_view() , name='index'),
    path('', views.home , name='home'),
]
