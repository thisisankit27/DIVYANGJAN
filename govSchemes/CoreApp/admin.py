from django.contrib import admin

from .models import SchemeList, VisitCounts, FilterCounts

# Register your models here.

admin.site.register(SchemeList)
admin.site.register(VisitCounts)
admin.site.register(FilterCounts)