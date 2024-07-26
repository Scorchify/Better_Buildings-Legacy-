from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'q1', 'q2', 'submitted_at', 'upvotes')
    readonly_fields = ('submitted_at',)  # Make submitted_at read-only