from django import forms
from .models import Problem
from django.contrib.auth.models import User


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['name', 'phone', 'email', 'description', 'priority']


class ProblemUpdateForm(forms.ModelForm):
    new_assigned_user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Problem
        fields = ['actions', 'status', 'assigned_user', 'resolved_user']

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        assigned_user = cleaned_data.get("assigned_user")
        resolved_user = cleaned_data.get("resolved_user")

        if status == 'resolved' and not resolved_user:
            self.add_error('resolved_user', 'You must choose Resolved user if you change status to resolved.')
        if status != 'resolved' and not assigned_user:
            self.add_error('assigned_user', 'You cannot leave Assigned user empty if you have not resolved the problem yet.')


