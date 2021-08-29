from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Member, Project, Task, StatusTask
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateTaskForm
from django.utils import timezone
from django.forms import ModelForm, ModelChoiceField
from .forms import CreateTaskForm

# Create your views here.
class MembersList(LoginRequiredMixin, ListView):
    model = Member
    context_object_name = 'members_list'
    template_name = 'projects/members_list.html'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task

class ProjectsList(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/projects_list.html'

    def get_context_data(self, **kwargs):

        pk = self.kwargs['pk']

        context = super(ProjectsList, self).get_context_data(**kwargs)
        context['projects_list'] = Project.objects.filter(member_owner=pk)
        member = Member.objects.filter(pk=pk)
        for m in member:
            context['member_name'] = m.name_short
        
        return context

class TasksList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'projects/tasks_list.html'

    def get_context_data(self, **kwargs):

        pk = self.kwargs['pk2']

        context = super(TasksList, self).get_context_data(**kwargs)
        
        context['tasks_list'] = Task.objects.filter(project=pk)
        project = Project.objects.filter(pk=pk)
        for p in project:
            context['project_name'] = p.сhapter_project
            member = Member.objects.filter(pk=p.member_owner.pk)
            context['project_pk'] = p.pk
            for m in member:
                context['member_name'] = m.name_short
                context['member_pk'] = m.pk
        
        return context

@login_required()
def create_task(request, pk1, pk2):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST,request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.author_id = request.user
            task.create_on = timezone.now()
            task.attachment = request.FILES['attachment']
            task.project = Project.objects.filter(pk=pk2).last()
            task.status_task=StatusTask.objects.all().first()
            task.save()
            return redirect('task_detail', member_pk=pk1, project_pk=pk2, pk=task.pk)
    else:
        form = CreateTaskForm()
    return render(
        request,
        'projects/create_task.html',
        {'form':form, 'pk1':pk1,'pk2':pk2}
    )
