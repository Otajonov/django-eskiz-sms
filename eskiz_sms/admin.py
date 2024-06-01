from django.contrib import admin
from .models import EskizSMS, SMSLog


@admin.register(EskizSMS)
class EskizSMSAdmin(admin.ModelAdmin):
    list_display = ('email', 'from_name', 'callback_url', 'last_updated', 'eskiz_token')
    
    def get_readonly_fields(self, request, obj=None):
        return ['last_updated', 'eskiz_token']


@admin.register(SMSLog)
class SMSLogAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'message', 'from_name', 'status', 'status_date',  'from_app', 'error_message')
    list_filter = ['status', 'from_app', 'from_name', 'status_date' ]
    search_fields = ['phone_number', 'message' ]
    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
