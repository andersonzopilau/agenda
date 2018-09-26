from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields = ['date', 'event', 'priority']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text','author', 'email', 'event']