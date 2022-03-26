from .models import Comment
from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class SomeForm(forms.Form):
    foo = SummernoteTextFormField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

