from django import forms

class InputBox(forms.Textarea):
    class Media:
        css = {
            "all": ["css/input.css"],  
        }

class LoginForm(forms.Form):
    class Media:
        css = {
            "all": ["css/login.css"]
        }
    Name = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Name (First and Last)",
            "class": "input-box",
            "autocomplete": "off",
            "rows": 2,
            "cols": 25
        }),
        label=''
    )
    School = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "School",
            "class": "input-box",
            "autocomplete": "off",
            "rows": 2,
            "cols": 25
        }),
        label=''
    )

    

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

