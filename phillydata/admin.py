from django.contrib import admin

from external_data_sync.admin import BaseDataSourceAdmin

from .models import PhillyDataSource


class PhillyDataSourceAdmin(BaseDataSourceAdmin):
    pass

admin.site.register(PhillyDataSource, PhillyDataSourceAdmin)
