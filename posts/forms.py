from django import forms

from posts.models import SelectedFood


class FoodForm(forms.ModelForm):
    class Meta:
        model = SelectedFood
        exclude = ['student','date1', 'date2', 'date3', 'date4', 'date5', 'date6', 'date7']