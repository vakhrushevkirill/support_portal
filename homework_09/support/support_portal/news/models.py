from django.db import models
from users.models import UserPortal


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    text = models.TextField()
    create_on = models.TimeField(default=0)
    commetns_count = models.IntegerField(null=True)
    author_id = models.ForeignKey(UserPortal, on_delete=models.DO_NOTHING)