
from django import forms

class fromsform(forms.Form):
    name=forms.CharField(
        label="enter u r Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'name'
            }
        )
    )
    email=forms.EmailField(
        label="email id",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email ID'
            }
        )
    )
    sal=forms.IntegerField(
        label='salary',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Salary'
            }
        )
    )
    loc=forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Location'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter Mobile',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile'
            }
        )
    )
    username=forms.CharField(
        label='Enter user name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'User Name'
            }
        )
    )
    password=forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )


class loginform(forms.Form):
    username = forms.CharField(
        label='Enter user name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User Name'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
