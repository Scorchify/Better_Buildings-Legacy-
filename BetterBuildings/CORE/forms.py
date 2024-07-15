from django import forms

class InputBox(forms.Textarea):
    class Media:
        css = {
            "all": ["css/input.css"],  
        }

class ReportingForm(forms.Form):
    q1 = forms.CharField(
        widget=InputBox(attrs={
            "placeholder": "Enter your response here!",
            "class": "input-box",
            "rows": 4,  
            "cols": 50  
        }),
        label=''
    )
    q2 = forms.ChoiceField(
        choices=[
            ('', 'Select'),  # Default option
            ('Bathrooms', 'Bathrooms'),
            ('Building', 'Building'),
            ('Other', 'Other')
        ],
        widget=forms.Select(attrs={
            "class": "select",
        }),
        label="How would you categorize your issue?"
    )

    def clean_q2(self):
        data = self.cleaned_data['q2']
        if data == '':
            raise forms.ValidationError("Please select a valid option.")
        return data
