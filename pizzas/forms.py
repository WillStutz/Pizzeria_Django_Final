from django import forms

from .models import * 

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pizza','comments']
        labels = {'pizza':'','comments':''}

        widgets = {'comments': forms.Textarea(attrs={'cols':80})}