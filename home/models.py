from django.db import models


# SKILLS
class HardSkill(models.Model):
    name = models.CharField("Savoir-faire", max_length=250)

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    name = models.CharField("Savoir-être", max_length=250)

    def __str__(self):
        return self.name


# JOB OFFER
class JobOffer(models.Model):
    name = models.CharField("Intitulé du poste", max_length=250)
    experience = models.IntegerField('Expérience souhaitée', null=True, blank=True)

    def __str__(self):
        return self.name


class JobHardSkill(models.Model):
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE, related_name='job_hardskills')
    hardskill = models.ForeignKey(HardSkill, verbose_name="Hard skills souhaité", on_delete=models.CASCADE)
    level = models.IntegerField("Niveau de compétence souhaité", default=1)  # 1 à 5

    def __str__(self):
        return f'{self.job} : {self.hardskill}'


class JobSoftSkill(models.Model):
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE, related_name='job_softskills')
    softskill = models.ForeignKey(SoftSkill, verbose_name="Soft skill souhaité", on_delete=models.CASCADE)
    level = models.IntegerField("Niveau de compétence souhaité", default=1)  # 1 à 5

    def __str__(self):
        return f'{self.job} : {self.softskill}'


# USER
class User(models.Model):
    email = models.EmailField('Adresse mail', unique=True)
    first_name = models.CharField('Prénom', max_length=100, null=True, blank=True)
    last_name = models.CharField('Nom', max_length=100, null=True, blank=True)
    experience = models.IntegerField('Années expérience', default=0)

    def __str__(self):
        return self.first_name


class UserSoftSkill(models.Model):
    user = models.ForeignKey(User, verbose_name="Utilisateur", on_delete=models.CASCADE)
    softskill = models.ForeignKey(SoftSkill, verbose_name='Soft skill', on_delete=models.CASCADE)
    level = models.IntegerField("Note / niveau", default=1)  # 1 à 5

    def __str__(self):
        return f'{self.user} : {self.softskill}'


class UserHardSkill(models.Model):
    user = models.ForeignKey(User, verbose_name="Utilisateur", on_delete=models.CASCADE)
    hardskill = models.ForeignKey(HardSkill, verbose_name="Hard skill", on_delete=models.PROTECT)
    level = models.IntegerField("Note / niveau", default=1)  # 1 à 5

    def __str__(self):
        return f'{self.user} : {self.hardskill}'
