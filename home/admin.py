from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export.formats.base_formats import XLSX, CSV
from .models import HardSkill, SoftSkill, JobOffer, JobHardSkill, JobSoftSkill, User, UserSoftSkill, UserHardSkill


class CustomImportExportMixin(ExportActionMixin):
    formats = [XLSX, CSV]


@admin.register(HardSkill)
class HardSkillAdmin(CustomImportExportMixin, ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(SoftSkill)
class SoftSkillAdmin(CustomImportExportMixin, ImportExportModelAdmin):
    list_display = ('name',)


class JobHardSkillInline(admin.TabularInline):
    model = JobHardSkill


class JobSoftSkillInline(admin.TabularInline):
    model = JobSoftSkill


@admin.register(JobOffer)
class JobOfferAdmin(CustomImportExportMixin, ImportExportModelAdmin):
    inlines = [
        JobHardSkillInline,
        JobSoftSkillInline,
    ]
    list_display = ('name', 'experience')


class UserSoftSkillInline(admin.TabularInline):
    model = UserSoftSkill


class UserHardSkillInline(admin.TabularInline):
    model = UserHardSkill


@admin.register(User)
class UserAdmin(CustomImportExportMixin, ImportExportModelAdmin):
    inlines = [
        UserHardSkillInline,
        UserSoftSkillInline,
    ]
    list_display = ('email', 'first_name', 'last_name', 'experience')
