from django import forms

class ReportingForm(forms.Form):
    q1 = forms.CharField(label="How would you categorize your issue?", max_length=500)
    q2 = forms.CharField(label="What is the issue and where is it occurring?", max_length=500)
