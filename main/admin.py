from django.contrib import admin
from main.models import Report, AdsDateTime


class AdsDateTimeInline(admin.TabularInline):
    model = AdsDateTime
    extra = 0
    can_delete = False
    readonly_fields = ['date_time']


class ReportAdmin(admin.ModelAdmin):
    inlines = [AdsDateTimeInline]


admin.site.register(Report, ReportAdmin)