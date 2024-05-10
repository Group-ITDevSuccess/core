from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import HardSkill, SoftSkill, JobOffer, JobHardSkill, JobSoftSkill, User, UserSoftSkill, UserHardSkill


# Define resources for import-export
class HardSkillResource(resources.ModelResource):
    class Meta:
        model = HardSkill


class SoftSkillResource(resources.ModelResource):
    class Meta:
        model = SoftSkill


class JobOfferResource(resources.ModelResource):
    class Meta:
        model = JobOffer


class JobHardSkillResource(resources.ModelResource):
    class Meta:
        model = JobHardSkill


class JobSoftSkillResource(resources.ModelResource):
    class Meta:
        model = JobSoftSkill


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UserSoftSkillResource(resources.ModelResource):
    class Meta:
        model = UserSoftSkill


class UserHardSkillResource(resources.ModelResource):
    class Meta:
        model = UserHardSkill


# Register models with import-export functionality
@admin.register(HardSkill)
class HardSkillAdmin(ImportExportModelAdmin):
    resource_class = HardSkillResource
    list_display = ('id', 'name')


@admin.register(SoftSkill)
class SoftSkillAdmin(ImportExportModelAdmin):
    resource_class = SoftSkillResource
    list_display = ('id', 'name')


@admin.register(JobOffer)
class JobOfferAdmin(ImportExportModelAdmin):
    resource_class = JobOfferResource
    list_display = ('id', 'name', 'experience')


@admin.register(JobHardSkill)
class JobHardSkillAdmin(ImportExportModelAdmin):
    resource_class = JobHardSkillResource
    list_display = ('id', 'job', 'hardskill', 'level')


@admin.register(JobSoftSkill)
class JobSoftSkillAdmin(ImportExportModelAdmin):
    resource_class = JobSoftSkillResource
    list_display = ('id', 'job', 'softskill', 'level')


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('id', 'email', 'first_name', 'last_name', 'experience')


@admin.register(UserSoftSkill)
class UserSoftSkillAdmin(ImportExportModelAdmin):
    resource_class = UserSoftSkillResource
    list_display = ('id', 'user', 'softskill', 'level')


@admin.register(UserHardSkill)
class UserHardSkillAdmin(ImportExportModelAdmin):
    resource_class = UserHardSkillResource
    list_display = ('id', 'user', 'hardskill', 'level')
