from django.contrib import admin
from .models import HardSkill, SoftSkill, JobOffer, JobHardSkill, JobSoftSkill, User, UserSoftSkill, UserHardSkill


@admin.register(HardSkill)
class HardSkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


class JobHardSkillInline(admin.TabularInline):
    model = JobHardSkill


class JobSoftSkillInline(admin.TabularInline):
    model = JobSoftSkill


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
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
class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserHardSkillInline,
        UserSoftSkillInline,
    ]
    list_display = ('email', 'first_name', 'last_name', 'experience')
