from django import forms

class ReportingForm(forms.Form):
    q1 = forms.CharField(label="q1", widget=forms.Textarea(attrs={"class": "input-box", "placeholder": "Enter your response here!"}))
    q2 = forms.CharField(label="q2", widget=forms.Textarea(attrs={"class": "input-box", "placeholder": "Enter your response here!"}))
