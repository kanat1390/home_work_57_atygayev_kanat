from django import forms
from tasks.models import Task
from tasks.services import get_type_query_set

class TaskForm(forms.ModelForm):
    types=forms.ModelMultipleChoiceField(queryset=get_type_query_set(), widget=forms.SelectMultiple(attrs={'class':'form-control form-control-custom'}))
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'types')
        widgets = {
            'summary':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control form-control-custom'}),
        }