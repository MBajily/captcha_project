from django.urls import path
from . import views

app_name = 'recaptcha_test'

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('success/', views.success, name='success'),
]