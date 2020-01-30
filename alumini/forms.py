from django import forms


'''class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
'''
Degree= [
    ('B.Tech', 'B.Tech'),
    ('MSc', 'MSc'),
    ('MCA', 'MCA'),
    ('M.Tech', 'M.Tech'),
    ]

class RegisterForm(forms.Form):
    registrationNo = forms.CharField(label="Registration No.",widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Registration No'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone Number'}), required=False)
    degree= forms.CharField(label='Degree', widget=forms.Select(choices=Degree))

class AluminiLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
