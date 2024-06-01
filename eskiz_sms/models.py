from django.db import models
from django.utils import timezone
import requests



class EskizSMS(models.Model):
    
    email = models.EmailField('Eskiz Email')
    password = models.CharField('Eskiz kabinetidan parol', max_length=255)
    from_name = models.CharField('Nickname (Birlamchi 4546)', max_length=255, blank=True, null=True)
    callback_url = models.URLField("Callback URL (Ixtiyoriy)", null=True, blank=True)

    eskiz_token = models.TextField("Token (Avtomatik yangilanadi)", null=True, blank=True)
    last_updated = models.DateTimeField("So'ngi yangilanish", default=timezone.now)

    class Meta:
        verbose_name = "Sozlama"
        verbose_name_plural = "Sozlamalar"
        
    def __str__(self):
        return self.email
    

    def update_token(self):
        
        payload = {
            'email': self.email,
            'password': self.password
        }
        
        response = requests.post("https://notify.eskiz.uz/api/auth/login", headers={}, data=payload)
        
        if response.status_code == 200:
            resp_data = response.json()
            
            self.last_updated = timezone.now()
            self.eskiz_token = resp_data.get('data', {}).get('token', '')
            self.save()
            
            return resp_data.get('data', {}).get('token', '')
        return None





class SMSLog(models.Model):
    phone_number = models.CharField('Telefon raqam', max_length=20)
    message = models.TextField('SMS matni')
    from_name = models.CharField('Qaysi nikdan', max_length=255)
    status = models.CharField('Holati', max_length=10)
    status_date = models.DateTimeField("Oxirgi o'zgarish", default=timezone.now)
    error_message = models.TextField('Xatolik', blank=True, null=True)
    from_app = models.CharField("Qaysi 'app'dan", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "SMS tarixi"
        verbose_name_plural = "SMSlar tarixi"
        
    def __str__(self):
        return f"{self.phone_number} - {self.message}"

def save_sms_log(phone_number, message, from_name, status, error_message=None, from_app=None):
    SMSLog.objects.create(
        phone_number=phone_number,
        message=message,
        from_name=from_name,
        status=status,
        error_message=error_message,
        from_app=from_app
    )
