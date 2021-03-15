from django import forms
from .models import ToDoListModel

class ToDoListForm(forms.ModelForm):
    class Meta():
        model=ToDoListModel
        fields=['title','description']