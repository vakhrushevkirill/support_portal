from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from django.contrib.auth.forms import (
#     AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
# )
# from django.db import router, transaction
# from django.http import Http404, HttpResponseRedirect
# from django.conf import settings


# Create your models here.
class UserPortal(AbstractUser):
    age = models.IntegerField(null=True)