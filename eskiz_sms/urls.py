from django.urls import path
from . import views

app_name = 'eskiz_sms'

urlpatterns = [
    path('send-sms/', views.send_sms_view, name='send_sms'),
]
