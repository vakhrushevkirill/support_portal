from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'text', 'attachment')

        labels = {
            'name': 'Название',
            'text': 'Текст',
            'attachment':'Вложения',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'attachment': forms.FileInput(),
        }