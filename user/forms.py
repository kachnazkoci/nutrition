from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


class DatePickerDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(DatePickerDateInput, self).__init__(*args, **kwargs)


class DateFieldSevenDaysFromNow(forms.DateField):
    widget = DatePickerDateInput

    def validate(self, value):
        super(DateFieldSevenDaysFromNow, self).validate(value)
        if value < timezone.now().date() + timedelta(days=7):
            raise ValidationError('Cannot create contact at earlier that 7 days from now')


class UserForm(forms.ModelForm):
    birth_date = forms.DateField(widget=DatePickerDateInput())
    created_date = forms.DateField(widget=DatePickerDateInput())
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active',
                   'date_joined']

    def clean_password(self):
        password = self.cleaned_data['password']
        hashed_password = make_password(password)
        return hashed_password

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=commit)
        return user


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    phone_number = forms.IntegerField()
    age = forms.IntegerField(min_value=1, max_value=99)
    contact_at = DateFieldSevenDaysFromNow()
    subscribe = forms.BooleanField()

    def clean_name(self):
        return self.data.get('name').lower()


# class BasalMetabolism(forms.ModelForm):
#     ACTIVITY_1 = 'office job, no activities'
#     ACTIVITY_2 = 'office job, training twice per week'
#     ACTIVITY_3 = 'office job, training 3-4 times per week'
#     ACTIVITY_4 = 'office job, training 6 times per week'
#     ACTIVITY_5 = 'manual job, training 3-4 times per week'
#     ACTIVITY_6 = 'manual job, training 6 times per week'
#
#     ACTIVITY_CHOICES = (
#         (ACTIVITY_1, 'office job, no activities'),
#         (ACTIVITY_2, 'office job, training twice per week'),
#         (ACTIVITY_3, 'office job, training 3-4 times per week'),
#         (ACTIVITY_4, 'office job, training 6 times per week'),
#         (ACTIVITY_5, 'manual job, training 3-4 times per week'),
#         (ACTIVITY_6, 'manual job, training 6 times per week'),
#     )
#
#     TARGET_1 = 'I would like lose weight'
#     TARGET_2 = 'I just want be as fit as I am'
#     TARGET_3 = 'I want gain muscles/weight'
#
#     TARGET_CHOICES = (
#         (TARGET_1, 'I would like lose weight'),
#         (TARGET_2, 'I just want be as fit as I am'),
#         (TARGET_3, 'I want gain muscles/weight'),
#
#     activity = forms.CharField(help_text='How active are you?', choices=ACTIVITY_CHOICES, max_length=255)
#     target = forms.CharField(help_text='What is your target?', choices=TARGET_CHOICES, max_length=255)
#     class Meta:
#         model = BasalMetabolism
#         fields = '__all__'


class RegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'birth_date', 'height', 'weight', 'title']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user
