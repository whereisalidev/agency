from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mail', views.mail, name='mail'),
    path('unsubscribed', views.unsubscribed, name='unsubscribed')
]
