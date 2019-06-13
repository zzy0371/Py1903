from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ["name","content","email","url"]
        widgets = {
            "content": forms.Textarea()
        }