from django import forms

from signup.models import Email

class SignupForm(forms.Form):
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(
                                 attrs={
                                     'id': 'email',
                                     'placeholder': 'Email Address'
                                 })
                             )

    def clean_email(self):
        import pdb; pdb.set_trace()
        email = self.cleaned_data['email']
        if Email.objects.get(email=email):
            raise forms.ValidationError('Too many characters ...')
        return email