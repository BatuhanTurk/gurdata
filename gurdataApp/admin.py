from django.contrib import admin
from .models import (
    UserGurdata,
    DataGurdata,
    DataDownloadGurdata,
    ContactGurdata,
    ContactModel,
    DataCategoryGurdata,
)

admin.site.register(UserGurdata)
class DataCategoryGurdataAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name', 'category_description']

admin.site.register(DataCategoryGurdata, DataCategoryGurdataAdmin)

admin.site.register(DataGurdata)

admin.site.register(DataDownloadGurdata)

admin.site.register(ContactGurdata)

admin.site.register(ContactModel)
