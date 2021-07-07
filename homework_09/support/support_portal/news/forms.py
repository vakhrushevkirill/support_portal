from django import forms
from .models import News

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'description', 'text')

        labels = {
            'title': 'Заголовок',
            'description': 'Краткое описание',
            'text':'Текст новости',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
            
