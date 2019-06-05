from django.conf.urls import url
from .views import index,list
urlpatterns = [
    url('index/',index),
    url('list/',list)
]