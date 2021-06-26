from django.db import models
from main.models import User


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    create_on = models.TimeField()
    commetns_count = models.IntegerField()
    author_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)