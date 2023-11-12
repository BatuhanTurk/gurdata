from django.contrib import admin
from .models import UserGurdata,DataGurdata,DataDownloadGurdata,ContactGurdata

admin.site.register(UserGurdata)
class UserGurdataAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email') 
admin.site.register(DataGurdata)

admin.site.register(DataDownloadGurdata)

admin.site.register(ContactGurdata)
