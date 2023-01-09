from django import forms
from .models import GitInTouch


class GitInTouchForm(forms.ModelForm):
    class Meta:
        model = GitInTouch
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GitInTouchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name.capitalize()
