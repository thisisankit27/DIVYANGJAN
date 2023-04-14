from django.contrib import admin

from .models import SchemeList, Counts

# Register your models here.

admin.site.register(SchemeList)
admin.site.register(Counts)