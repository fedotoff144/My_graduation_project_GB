from django import forms
import datetime


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_name(self):
        """Bad example change standart method min_length."""
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('The name must be bigger than 3 literal')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not (email.endswith('vk.tem') or email.endswith('corp.mail.ru')):
            raise forms.ValidationError('Use corporate mail.')
        return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthday = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ManyFieldsForWidget(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Enter user name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.com'}))
    age = forms.IntegerField(min_value=18,
                             widget=forms.NumberInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Age'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control',
                                                             'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('I', 'It')],
                               widget=forms.RadioSelect(attrs={'class': 'form-control'}))
    message = forms.CharField(max_length=500,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
    image = forms.ImageField()