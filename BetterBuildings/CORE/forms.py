from django import forms

class ReportingForm(forms.Form):
    q1 = forms.CharField(label="q1", max_length=500)
    q2 = forms.CharField(label="q2", max_length=500)