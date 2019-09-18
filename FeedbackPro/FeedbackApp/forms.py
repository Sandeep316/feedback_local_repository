from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    location=forms.CharField(
        label="Enter Your City",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your City'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )