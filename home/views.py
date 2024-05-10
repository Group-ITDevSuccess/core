from django.shortcuts import render
from django.db.models import Count, F, Q, When, Case
from .models import JobOffer, JobHardSkill, JobSoftSkill, User, UserHardSkill, UserSoftSkill

from django.db.models import F, FloatField, Sum
from django.db.models.functions import Coalesce


def get_matching_job_offers(user_id):
    user_hard_skills = UserHardSkill.objects.filter(user_id=user_id)
    user_soft_skills = UserSoftSkill.objects.filter(user_id=user_id)

    matching = (
        Coalesce(
            Sum(
                Case(
                    When(job_hardskills__hardskill_id__in=user_hard_skills.values('hardskill_id'),
                         job_hardskills__level__lte=F('job_hardskills__level')),
                    then=1.0
                )
            ), 0.0) * (50 / 100) +
        Coalesce(
            Sum(
                Case(
                    When(job_softskills__softskill_id__in=user_soft_skills.values('softskill_id'),
                         job_softskills__level__lte=F('job_softskills__level')),
                    then=1.0
                )
            ), 0.0) * (30 / 100) +
        (F('experience') * (20 / 100)) * 100
    )

    job_offers = JobOffer.objects.annotate(
        matching=matching,
    ).order_by('-matching')

    return job_offers


def home(request):
    users = User.objects.all()
    user_job_matches = {}

    for user in users:
        user_id = user.id
        matching_job_offers = get_matching_job_offers(user_id)
        user_job_matches[user] = matching_job_offers

    context = {
        'user_job_matches': user_job_matches
    }
    return render(request, 'home/index.html', context)
