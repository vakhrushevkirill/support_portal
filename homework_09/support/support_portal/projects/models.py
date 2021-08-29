from django.db import models
from users.models import UserPortal
from django.utils import timezone

# Create your models here.
class StatusMember(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class StatusTask(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status
    

class Member(models.Model):
    name_short = models.CharField(max_length=100)
    name_full = models.CharField(max_length=200)
    member_status = models.ForeignKey(StatusMember, on_delete=models.DO_NOTHING)

    def display_status(self):
        return self.member_status

    def __str__(self):
        return self.name_full

class Project(models.Model):
    сhapter_project = models.CharField(max_length=200)
    member_owner = models.ForeignKey(Member, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.member_owner}.{self.сhapter_project}'

class Task(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    create_on = models.TimeField(default=timezone.now)
    commetns_count = models.IntegerField(blank=True, null=True)
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True, null=True)
    status_task = models.ForeignKey(StatusTask, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    author_id = models.ForeignKey(UserPortal, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    author_id = models.ForeignKey(UserPortal, on_delete=models.DO_NOTHING)