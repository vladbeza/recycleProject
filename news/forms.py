from django import forms
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=CKEditorWidget())
