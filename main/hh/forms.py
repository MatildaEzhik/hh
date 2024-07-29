from django import forms

from hh.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['dream_job', 'name', 'surname', 'lastname', 'date_of_birth', 'email', 'phone', 'skills', 'experience', 'education', 'gender']
