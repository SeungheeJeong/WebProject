from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Recruit)
class RecruitAdmin(admin.ModelAdmin):
    """Custom Recruit Admin"""
    list_display = (
        "subject",
        "select",
        "personnel",
        "content",
        "create_date",
    )


@admin.register(models.Applicant)
class Applicant(admin.ModelAdmin):
    list_display = (
        "question",
        "content",
        "create_date",
    )
