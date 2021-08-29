from django.contrib import admin
from .models import Member, Project, StatusMember, Task, StatusTask
# Register your models here.
@admin.register(StatusMember)
class StatusMemberAdmin(admin.ModelAdmin):
    list_display = ('status',)
    fields = ['status']

@admin.register(StatusTask)
class StatusTaskAdmin(admin.ModelAdmin):
    list_display = ('status',)
    fields = ['status']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name_short', 'name_full', 'display_status')
    fields = ['name_short', 'name_full', 'member_status']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('сhapter_project', 'member_owner')
    fields = ['сhapter_project', 'member_owner']


#admin.site.register(Project)
#admin.site.register(Member)
#admin.site.register(StatusMember, StatusMemberAdmin)
admin.site.register(Task)
