from django.shortcuts import render
from django.http import HttpResponse

from .models import EskizSMS, save_sms_log
import requests



def send_sms(phone, message, from_name=None, from_app=None):
    
   
    eskiz = EskizSMS.objects.first() 
    
    url = "https://notify.eskiz.uz/api/message/sms/send"
    
    payload = {
            'mobile_phone': phone,
            'message': message[:160],  # Limit to 160 characters
            'from': from_name or eskiz.from_name or "4546",
            'callback_url': eskiz.callback_url
        }


    if eskiz:
        
        response = requests.post(url, headers={'Authorization': f'Bearer { eskiz.eskiz_token or eskiz.update_token() }'}, data=payload)

        if response.status_code == 200:
            save_sms_log(phone, message, from_name or eskiz.from_name or "4546", 'SENT', from_app=from_app)
            return True
        else:
            error_message = response.text
            save_sms_log(phone, message, from_name or eskiz.from_name or "4546", 'ERROR', error_message, from_app=from_app)
            requests.post(url, headers={'Authorization': f'Bearer { eskiz.update_token() }'}, data=payload)
            return False

    return False

def send_sms_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        message = request.POST.get('sms')

        if send_sms(phone, message, from_name=request.POST.get('from') ):
            return HttpResponse('SMS sent successfully!')
        else:
            return HttpResponse('Failed to send SMS.')

    return render(request, 'send_sms.html')
