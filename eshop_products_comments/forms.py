from django import forms


class UserNewCommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'نظر خود خود را وارد کنید', 'class': 'form-control'}),
        label='نظر خود را وارد کنید')