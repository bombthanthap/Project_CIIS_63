from django import forms
from django_countries.fields import CountryField

#DataFlair #Form
class SignUp(forms.Form):
    CHOICES= (
    ('Ms.', 'Ms.'),
    ('Miss.', 'Miss.'),
    ('Mr.', 'Mr.'),
    )
    select = forms.CharField(widget=forms.Select(choices=CHOICES))
    first_name = forms.CharField()
    first_name.widget = forms.TextInput(attrs={'size': 10, 'class': 'form-control',})
    last_name = forms.CharField()
    last_name.widget = forms.TextInput(attrs={'size': 10, 'class': 'form-control',})
    nationality = CountryField(blank_label='(Select country)',).formfield()
    

   
   
   
    email = forms.CharField()
    email.widget = forms.TextInput(attrs={'size': 10, 'class': 'form-control','type':'email'})
    password = forms.CharField(widget = forms.PasswordInput)
    password.widget = forms.TextInput(attrs={'size': 10, 'class': 'form-control','type':'password'})
    re_password = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)
    re_password.widget = forms.TextInput(attrs={'size': 10, 'class': 'form-control','type':'password'})

    ID_CARD_NO = forms.CharField(label="ID CARD NO. /  Passport NO.",max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'identify','name':'identify'}))
  
