from django import forms
from food.models import Food, Recipe
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError


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


class FoodForm(forms.ModelForm):
    created = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Food
        fields = '__all__'

    def save(self, commit=True):
        user = super(FoodForm, self).save(commit=commit)
        return user


class RecipeForm(forms.ModelForm):
    created = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Recipe
        # fields = '__all__'
        fields = ['name', 'kcal','protein','fats','carbs','food']

    def save(self, commit=True):
        recipe = super(RecipeForm, self).save(commit=commit)
        return recipe


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
