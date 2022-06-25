from django.contrib import admin
from .models import news, record, message, staff

admin.site.register(news)
admin.site.register(record)
admin.site.register(message)
admin.site.register(staff)