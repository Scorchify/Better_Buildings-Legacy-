from django import forms

class ReportingForm(forms.Form):
    q1 = forms.CharField(widget=forms.Textarea(attrs={"class": "input-box", "placeholder": "Enter your response here!"}))
    q2 = forms.CharField(widget=forms.Textarea(attrs={"class": "input-box", "placeholder": "Enter your response here!"}))
