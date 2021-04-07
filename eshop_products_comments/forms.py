from django import forms
from ckeditor.widgets import CKEditorWidget


class UserNewCommentForm(forms.Form):
    text = forms.CharField(
        widget=CKEditorWidget(),
        label='نظر خود را وارد کنید')
