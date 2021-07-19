from django.contrib import admin
from .models import UserPortal
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(UserPortal, UserAdmin)
